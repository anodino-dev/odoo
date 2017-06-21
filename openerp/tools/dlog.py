import inspect
import logging

active = True

def dlog(fn):
    varList, _, _, default = inspect.getargspec(fn)
    d = {}
    log = logging.getLogger(fn.__module__)
    if default is not None:
        d = dict((varList[-len(default):][i], v) for i, v in enumerate(default))
    def f(*argt, **argd):
        if active :
            log.info('>>>Enter %s' % fn)
        d.update(dict((varList[i], v) for i, v in enumerate(argt)))
        d.update(argd)
        if active :
            for c in d.iteritems():
                log.info('%s = %s' % c)
        ret = fn(*argt, **argd)
        if active :
            log.info('<<<Exit %s' % fn)
            if type(ret)!=tuple:
                log.info('return: %s' % ret)
            else:
                ff = 'return: ('+ ( len(ret) * '%s,' )+')'
                log.info(ff % ret)
        return ret
    return f
