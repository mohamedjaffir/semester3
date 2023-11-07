

import sim
import sys
import tkinter
print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')

    # Now try to retrieve data in a blocking fashion (i.e. a service call):
    res,objs=sim.simxGetObjects(clientID,sim.sim_handle_all,sim.simx_opmode_blocking)
    if res==sim.simx_return_ok:
        print ('Number of objects in the scene: ',len(objs))
    else:
        print ('Remote API function call returned with error code: ',res)
_,rm=sim.simxGetObjectsHandle(clientID,'RM',sim.simx_opmode_oneshot_wait)
_,lm=sim.simxGetObjectsHandle(clientID,'LM',sim.simx_opmode_oneshot_wait)
root=tkinter.TK()
def onclick(args):
    if args==1:
        sim.simxsetJointTargetvelocity(clientID,rm,2,sim.simx_opmode_streaming)
        sim.simxsetJointTargetvelocity(clientID,lm,2,sim.simx_opmode_streaming)
    if args==2:
        sim.simxSetJointTargetVelocity(clientID,rm,-2,sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(clientID,lm, -2, sim.simx_opmode_streaming)
    if args==3:
        sim.simxSetJointTargetVelocity(clientID, rm, 5, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(clientID, lm, 0, sim.simx_opmode_streaming)
btn1=tkinter.Button(root,text='Front',bg='green',command=lambda:oneclick(1))
btn2=tkinter.Button(root,text='back',bg='green',command=lambda:oneclick(2))
btn3=tkinter.Button(root,text='Left',bg='green',command=lambda:oneclick(3))
btn4=tkinter.Button(root,text='Right',bg='green',command=lambda:oneclick(4))
btn5=tkinter.Button(root,text='stop',bg='red',command=lambda:oneclick(5))

btn1.pack(side='top')
btn2.pack(side='bottom')
btn3.pack(side='left')
btn4.pack(side='right')
btn5.pack(padx=50,pady=20,side=tkinter.LEFT)

root.mainloop()