#!/usr/bin/env ruby
# frozen_string_literal: true

require 'open3'
require 'yaml'

root = __dir__
cases = YAML.load_file(File.join(root, 'test-cases.yaml')).fetch('cases')
failures = []

cases.each do |test_case|
  args = ['ruby', File.join(root, 'resolve.rb'), '--profile', test_case.fetch('profile'), '--verify']
  test_case.fetch('concepts').each { |concept| args.concat(['--concept', concept]) }
  output, status = Open3.capture2e(*args)
  expected = test_case.fetch('expect_sources').map { |source| "- #{source}:" }
  expected_decisions = test_case.fetch('expect_decisions').map { |decision| "- #{decision} (" }
  decisions_section = output.split("sources:", 2).first
  actual_decisions = decisions_section.lines.map { |line| line[/^  - ([^(]+) \(/, 1] }.compact
  unexpected_decisions = actual_decisions - test_case.fetch('expect_decisions')
  passed = status.success? && expected.all? { |source| output.include?(source) } &&
    expected_decisions.all? { |decision| output.include?(decision) } && unexpected_decisions.empty?
  failures << "#{test_case['id']}: #{output}" unless passed
  puts "#{passed ? 'PASS' : 'FAIL'} #{test_case['id']}"
end

abort failures.join("\n") unless failures.empty?
