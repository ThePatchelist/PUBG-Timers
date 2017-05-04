class TkRepeatingTask(object):

    def __init__( self, tkRoot, taskFuncPointer, freqencyMillis ):
        self.__tk_   = tkRoot
        self.__func_ = taskFuncPointer
        self.__freq_ = freqencyMillis
        self.__isRunning_ = False

    def isRunning( self ) : return self.__isRunning_

    def start( self ) :
        self.__isRunning_ = True
        self.__onTimer()

    def stop( self ) : self.__isRunning_ = False

    def __onTimer( self ):
        if self.__isRunning_ :
            self.__func_()
            self.__tk_.after( self.__freq_, self.__onTimer )