#!/usr/bin/env ruby
# Validate YAML and local Markdown links without Python package dependencies.
require 'yaml'
require 'pathname'

root = Pathname.new(__dir__).parent
skill = root.join('skills/landing-page-strategist')
content = skill.join('SKILL.md').read
frontmatter = content.match(/\A---\n(.*?)\n---\n/m)
abort 'Missing YAML frontmatter' unless frontmatter
data = YAML.safe_load(frontmatter[1])
abort 'Invalid skill name' unless data['name'] == 'landing-page-strategist'
abort 'Invalid description' unless data['description'].is_a?(String) && data['description'].length.between?(1, 1024)
abort 'Unexpected frontmatter keys' unless (data.keys - %w[name description metadata license allowed-tools]).empty?
metadata = YAML.safe_load(skill.join('agents/openai.yaml').read)
interface = metadata.fetch('interface')
abort 'Missing invocation' unless interface.fetch('default_prompt').include?('$landing-page-strategist')
abort 'Invalid short description' unless interface.fetch('short_description').length.between?(25, 64)

files = [root.join('README.md'), root.join('INSTALL.md')] + root.join('docs').glob('*.md') + skill.glob('**/*.md')
files.each do |file|
  file.read.scan(/\]\(([^)]+)\)/).flatten.each do |link|
    next if link.match?(/\A(?:https?:|#|mailto:)/)
    abort "Missing local link in #{file.relative_path_from(root)}: #{link}" unless file.dirname.join(link.split('#').first).exist?
  end
end
puts "Valid metadata and local links in #{files.length} Markdown files."
