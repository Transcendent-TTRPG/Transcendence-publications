#!/usr/bin/env ruby
# frozen_string_literal: true

# Deterministic resolver for the canonical retrieval layer. It returns references,
# never an uncited prose answer or a full chapter dump.
require 'optparse'
require 'yaml'
require 'pathname'

ROOT = Pathname.new(__dir__).join('../..').realpath
RETRIEVAL = Pathname.new(__dir__)

options = { concepts: [], verify: false }
OptionParser.new do |parser|
  parser.banner = 'Usage: ruby resolve.rb --profile PROFILE [--concept ID] [--verify]'
  parser.on('--profile ID', 'Retrieval profile id') { |value| options[:profile] = value }
  parser.on('--concept ID', 'Additional concept id; repeatable') { |value| options[:concepts] << value }
  parser.on('--verify', 'Validate manifest paths and registry references') { options[:verify] = true }
end.parse!

abort 'Missing --profile.' unless options[:profile]

manifest = YAML.load_file(RETRIEVAL.join('source-manifest.yaml'))
concept_registry = YAML.load_file(RETRIEVAL.join('concept-registry.yaml'))
profiles = YAML.load_file(RETRIEVAL.join('retrieval-profiles.yaml'))
decisions = YAML.load_file(ROOT.join('canon/decisions/registry.yaml'))

profile = profiles.fetch('profiles').find { |entry| entry['id'] == options[:profile] }
abort "Unknown profile: #{options[:profile]}" unless profile

concepts_by_id = concept_registry.fetch('concepts').to_h { |entry| [entry['id'], entry] }
requested_ids = profile.fetch('baseline_concepts', []) + options[:concepts]
unknown = requested_ids.uniq.reject { |id| concepts_by_id.key?(id) }
abort "Unknown concept(s): #{unknown.join(', ')}" unless unknown.empty?

source_ids = requested_ids.uniq.flat_map { |id| concepts_by_id.fetch(id).fetch('primary_sources') }.uniq
sources_by_id = manifest.fetch('sources').to_h { |entry| [entry['id'], entry] }
missing_sources = source_ids.reject { |id| sources_by_id.key?(id) }
abort "Unknown source(s): #{missing_sources.join(', ')}" unless missing_sources.empty?

if options[:verify]
  failed = sources_by_id.values.reject { |source| ROOT.join(source.fetch('path')).file? }
  abort "Missing source path(s): #{failed.map { |source| source['id'] }.join(', ')}" unless failed.empty?
  invalid_decisions = decisions.fetch('decisions', []).select { |entry| entry['status'] == 'approved' && entry['id'].to_s.empty? }
  abort 'Approved decision without an id.' unless invalid_decisions.empty?
end

relevant_decisions = decisions.fetch('decisions', []).select do |entry|
  entry['status'] == 'approved' &&
    (entry.fetch('related_concepts', []) & requested_ids.uniq).any?
end

puts "profile: #{profile['id']}"
puts "context_budget: #{profile['context_budget']}"
puts "concepts: #{requested_ids.uniq.join(', ')}"
puts 'decisions:'
relevant_decisions.each do |entry|
  puts "  - #{entry['id']} (#{entry['scope']})"
end
puts 'sources:'
source_ids.each do |id|
  source = sources_by_id.fetch(id)
  puts "  - #{source['id']}: #{source['path']}"
end
