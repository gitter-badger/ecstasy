#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import ecstasy

def main():

	text = "<Beware><(0) the <Jabberwock, my <son>>>!\n"\
		   "The <jaws> <(-2)that> <bite>, <(-1)the> <(2)claws> that <(3)catch>!\n"\
		   "<(0)One>, <two>! <(0!)One>, <(!)two>!\n"\
		   "The <(0,1)vorpal> <blade went> <snicker-<snack>>!"

	formats = [
		ecstasy.Fill.Yellow,
		ecstasy.Color.Yellow | ecstasy.Fill.Blue,
		ecstasy.Style.Blink | ecstasy.Color.Cyan,
		ecstasy.Fill.Magenta | ecstasy.Style.Blink | ecstasy.Color.White,
		ecstasy.Style.Invert,
		ecstasy.Style.Hidden
	]

	always = {
		("two", "blade went"): ecstasy.Color.Red | ecstasy.Fill.White,
		"Beware": ecstasy.Color.Yellow | ecstasy.Fill.Red | ecstasy.Style.Underline
	}

	beauty = ecstasy.beautify(text,
							  ecstasy.Color.Red,
							  formats,
							  always,
							  One=ecstasy.Fill.Cyan)

	print(beauty)

if __name__ == "__main__":

	main()
