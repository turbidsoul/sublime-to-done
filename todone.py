#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Turbidsoul Chen
# @Date:   2014-06-11 11:30:17
# @Last Modified by:   Turbidsoul Chen
# @Last Modified time: 2014-06-19 16:10:55

import sublime
import sublime_plugin


class CompleteTaskCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        point = self.view.sel()[0]
        cur_line_region = self.view.full_line(point)
        old_line = self.view.substr(cur_line_region)
        task_content = old_line.lstrip()
        indent = ''
        for c in old_line:
            if not c in [' ', '\t']:
                break
            indent += c
        new_line = indent
        if task_content[1] == '+':
            new_line += task_content[1:]
        elif task_content[1] == '.':
            new_line +=  "+" + task_content[1:]
        else:
            new_line += "+" + task_content
        self.view.replace(edit, cur_line_region, new_line)
        sublime.status_message("Complete Task: %s" % task_content)
        sublime.run_command('sub_notify', {'title': 'ToDone Complete Task:', 'msg': old_line.lstrip(), 'sound': False})


class CancelTaskCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        point = self.view.sel()[0]
        cur_line_region = self.view.full_line(point)
        old_line = self.view.substr(cur_line_region)
        task_content = old_line.lstrip()
        indent = ''
        for c in old_line:
            if not c in [' ', '\t']:
                break
            indent += c
        new_line = indent
        if task_content[0] == '.':
            new_line += task_content[1:]
        elif task_content[0] == '+':
            new_line += '.' + task_content[1:]
        else:
            new_line += '.' + task_content
        self.view.replace(edit, cur_line_region, new_line)
        sublime.status_message("Cancel Task: %s" % task_content)
        sublime.run_command('sub_notify', {'title': 'ToDone Cancel Task:', 'msg': old_line.lstrip(), 'sound': False})


class EmergencyTaskCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        point = self.view.sel()[0]
        cur_line_region = self.view.full_line(point)
        old_line = self.view.substr(cur_line_region)
        task_content = old_line.lstrip()
        indent = ''
        for c in old_line:
            if not c in [' ', '\t']:
                break
            indent += c
        new_line = indent
        if task_content[0] == '!':
            new_line += task_content[1:]
        elif task_content[0] in ['+', '.'] and task_content[1] == '!':
            new_line += task_content[0] + task_content[2:]
        elif task_content[0] in ['+', '.'] and task_content[1] == '-':
            new_line += task_content[0] + '!' + task_content[1:]
        else:
            new_line += '!' + task_content
        self.view.replace(edit, cur_line_region, new_line)
        sublime.status_message("Emergency Task: %s" % task_content)
        sublime.run_command('sub_notify', {'title': 'ToDone Emergency Task:', 'msg': old_line.lstrip(), 'sound': False})

