#!/usr/bin/python3

import argparse

def build(args):
  print("start building")

def install(args):
  print("start installing")

def clean(args):
  print("start cleaning")

def main():
  parser = argparse.ArgumentParser(desciption = 'build project')
  subparsers = parser.add_subparser(help = 'sub command help')
  cmd_build_parser = subparsers.add_parser('build', help = 'build project')
  cmd_build_parser.set_defaults(func = build)
  cmd_install_parser = subparsers.add_parser('install', help = 'install products')
  cmd_install_parser.set_defaults(func = install)
  cmd_clean_parser = subparsers.add_parser('clean', help = 'clean project')
  cmd_clean_parser.set_defaults(func = clean)

  arsgs = parser.parse_args()
  args.func(args)

if __name__ == '__main__':
  main()
