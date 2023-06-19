from flask import Flask, render_template, request, redirect


def render_fill_room(heading, tab):
    return render_template('fill-room-monitor.html', heading=heading, prod_line=tab)
