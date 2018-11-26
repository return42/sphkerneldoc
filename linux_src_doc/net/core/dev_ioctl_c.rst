.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/dev_ioctl.c

.. _`register_gifconf`:

register_gifconf
================

.. c:function:: int register_gifconf(unsigned int family, gifconf_func_t *gifconf)

    register a SIOCGIF handler

    :param family:
        Address family
    :type family: unsigned int

    :param gifconf:
        Function handler
    :type gifconf: gifconf_func_t \*

.. _`register_gifconf.description`:

Description
-----------

Register protocol dependent address dumping routines. The handler
that is passed must not be freed or reused until it has been replaced
by another handler.

.. _`dev_load`:

dev_load
========

.. c:function:: void dev_load(struct net *net, const char *name)

    load a network module

    :param net:
        the applicable net namespace
    :type net: struct net \*

    :param name:
        name of interface
    :type name: const char \*

.. _`dev_load.description`:

Description
-----------

If a network interface is not present and the process has suitable
privileges this function loads the module. If module loading is not
available in this kernel then it becomes a nop.

.. _`dev_ioctl`:

dev_ioctl
=========

.. c:function:: int dev_ioctl(struct net *net, unsigned int cmd, struct ifreq *ifr, bool *need_copyout)

    network device ioctl

    :param net:
        the applicable net namespace
    :type net: struct net \*

    :param cmd:
        command to issue
    :type cmd: unsigned int

    :param ifr:
        *undescribed*
    :type ifr: struct ifreq \*

    :param need_copyout:
        *undescribed*
    :type need_copyout: bool \*

.. _`dev_ioctl.description`:

Description
-----------

Issue ioctl functions to devices. This is normally called by the
user space syscall interfaces but can sometimes be useful for
other purposes. The return value is the return from the syscall if
positive or a negative errno code on error.

.. This file was automatic generated / don't edit.

