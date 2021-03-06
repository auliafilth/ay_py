#!/usr/bin/python
#\file    mikata2_off.py
#\brief   Turn off the Mikata arm (using TRobotMikata2).
#\author  Akihiko Yamaguchi, info@akihikoy.net
#\version 0.1
#\date    Jun.01, 2018
from _path import *
from ay_py.core import *
from ay_py.ros import *
from ay_py.ros.rbt_mikata2 import *

if __name__=='__main__':
  rospy.init_node('mikata_off')
  robot= TRobotMikata2()
  print 'Initializing...'
  robot.Init()
  rospy.sleep(0.1)
  print 'Done.'

  CPrint(1, 'Robot is relaxing...')
  for effort in range(5,-1,-1):  
    robot.mikata.MoveTo({jname:q for (jname,q) in zip(robot.JointNames(),robot.Q(arm=0))}, blocking=False)
    robot.mikata.SetPWM({jname:effort for jname in robot.JointNames()})
    robot.EndEff().Move(robot.EndEff().Position(), max_effort=effort)
    rospy.sleep(0.5)

  for i in range(3,0,-1):  
    CPrint(1, 'Torque is disabled after {} sec...'.format(i))
    rospy.sleep(1.0)
  robot.mikata.DisableTorque()

  robot.Cleanup()
