#!/bin/env python3

import openai
import sys
import os

openai.Model.delete(sys.argv[1])
