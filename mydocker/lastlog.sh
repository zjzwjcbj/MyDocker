#!/bin/bash
#记录用户登录记录

lastlog | sed "1d" >> /.logs/lastlog
