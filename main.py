from multiprocessing import Process, Pipe

gameConn, servConn = Pipe()

from CodeD import game
from server import serv

gameProcess = Process(target=game, args=(gameConn))
servProcess = Process(target=serv, args=(servConn))

gameProcess.start()
servProcess.start()

gameProcess.join()
servProcess.terminate()