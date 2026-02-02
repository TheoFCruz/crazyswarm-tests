"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from crazyflie_py import Crazyswarm
import numpy as np


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    pos1 = np.array([0.0, 0.5, 0.0])
    pos2 = np.array([0.0, -0.5, 0.0])

    height = 0.5
    takeoff_duration = 3

    cfnames = list(allcfs.crazyfliesByName.keys())
    cf1 = cfnames[0]
    cf2 = cfnames[1]

    allcfs.takeoff(height, takeoff_duration)
    timeHelper.sleep(5)

    # first position
    allcfs.crazyfliesByName[cf1].goTo(pos1 + np.array([0.0,0.0,height]), 0.0, 3.0)
    allcfs.crazyfliesByName[cf2].goTo(pos2 + np.array([0.0,0.0,height]), 0.0, 3.0)
    timeHelper.sleep(5)

    # first position
    allcfs.crazyfliesByName[cf1].goTo(pos2 + np.array([0.0,0.0,height]), 0.0, 3.0)
    allcfs.crazyfliesByName[cf2].goTo(pos1 + np.array([0.0,0.0,height]), 0.0, 3.0)
    
    timeHelper.sleep(5)
    allcfs.land(0.05, takeoff_duration)

if __name__ == '__main__':
    main()
