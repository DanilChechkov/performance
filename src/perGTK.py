#!/usr/bin/python3
import gi
import os
import sys
import subprocess


#subprocess.Popen(['pkexec','python3'])

gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from os.path import abspath
path = os.path.abspath(os.path.dirname(__file__)) + '/'

def changeMode(mode):
    for core in range (os.cpu_count()):
        scg = open('/sys/devices/system/cpu/cpu%s/cpufreq/scaling_governor'%str(core),'w')
        scg.write(mode)
        scg.close()
        scg = open('/sys/devices/system/cpu/cpu%s/cpufreq/scaling_max_freq'%str(core),'w')

        ar = open('/sys/devices/system/cpu/cpu%s/cpufreq/scaling_available_frequencies'%str(core),'r').readlines()[0].split()
        ar.sort()

        dicta = {'performance': -1,
                'powersave' : 0,
                'conservative' : int(len(ar)/2)}
        scg.write(ar[dicta[mode]])

    dicta = {'performance': 'max_performance',
            'conservative' : 'medium_power',
            'powersave' : 'min_power'}
    hosts = os.listdir('/sys/class/scsi_host/')
    for host in hosts:
        if os.path.exists('/sys/class/scsi_host/%s/link_power_management_policy'%host):
            hostf = open('/sys/class/scsi_host/%s/link_power_management_policy'%host,'w')
            hostf.write(dicta[mode])  

class auth:
    def __init__(self):
        self.window_is_hidden = False
    
    def passins(self,*args):
        p = subprocess.Popen(['sudo', '-A'] + ['python3'] + sys.argv, stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        p.communicate(pasbox.get_text() + '\n')
        sys.exit(0)

class Handler:
    def __init__(self):
        self.window_is_hidden = False

    def maxp(self,*args):
        if sw1.get_active():
            sw2.set_active(False)
            sw3.set_active(False)
            changeMode('performance')

    def midp(self,*args):
        if sw2.get_active():
            sw1.set_active(False)
            sw3.set_active(False)
            changeMode('conservative')
            
    def minp(self,*args):
        if sw3.get_active():
            sw1.set_active(False)
            sw2.set_active(False)
            changeMode('powersave')

ar = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies').readlines()[0].split()
ar.sort()

builder = Gtk.Builder()
builder.add_from_file(path+'GTKper.glade')

builder.connect_signals(Handler())

window = builder.get_object('window1')
sw1 = builder.get_object('sw1')
sw2 = builder.get_object('sw2')
sw3 = builder.get_object('sw3')
sw2.set_active(True)

window.connect('destroy',Gtk.main_quit)
window.show_all()
Gtk.main()

#if os.getuid() !=0: 
    #lnAPP = 'pkexec env DISPLAY="$DISPLAY" XAUTHORITY="$XAUTHORITY"'.split()
    #lnAPP.append(path+"perGTK.py")
    #subprocess.Popen(lnAPP)
    #pb = Gtk.Builder()
    #pb.add_from_file(path+'PassDi.glade')
    #pb.connect_signals(auth())
    #paswin = pb.get_object('passwin')
    #pasbox = pb.get_object('passbox')
    #pasbut = pb.get_object('button1')

    #paswin.connect('destroy',Gtk.main_quit)
    #paswin.show_all()
    #Gtk.main()
#else:
    #subprocess.Popen(['pkexec','python3'])
    #builder = Gtk.Builder()
    #builder.add_from_file(path+'GTKper.glade')

    #builder.connect_signals(Handler())

    #window = builder.get_object('window1')
    #sw1 = builder.get_object('sw1')
    #sw2 = builder.get_object('sw2')
    #sw3 = builder.get_object('sw3')
    #sw2.set_active(True)

    #window.connect('destroy',Gtk.main_quit)
    #window.show_all()
    #Gtk.main()