#!/usr/bin/env ruby
arg = ARGV[0]

from = arg.scan(/((?<=from:)[^\]]+)/).join
to = arg.scan(/((?<=to:)[^\]]+)/).join
flags = arg.scan(/((?<=flags:)[^\]]+)/).join

puts "#{from},#{to},#{flags}"
