.. -*- coding: utf-8; mode: rst -*-

===========
dev_ioctl.c
===========


.. _`register_gifconf`:

register_gifconf
================

.. c:function:: int register_gifconf (unsigned int family, gifconf_func_t *gifconf)

    register a SIOCGIF handler

    :param unsigned int family:
        Address family

    :param gifconf_func_t \*gifconf:
        Function handler



.. _`register_gifconf.description`:

Description
-----------

Register protocol dependent address dumping routines. The handler
that is passed must not be freed or reused until it has been replaced
by another handler.



.. _`dev_load`:

dev_load
========

.. c:function:: void dev_load (struct net *net, const char *name)

    load a network module

    :param struct net \*net:
        the applicable net namespace

    :param const char \*name:
        name of interface



.. _`dev_load.description`:

Description
-----------

If a network interface is not present and the process has suitable
privileges this function loads the module. If module loading is not
available in this kernel then it becomes a nop.



.. _`dev_ioctl`:

dev_ioctl
=========

.. c:function:: int dev_ioctl (struct net *net, unsigned int cmd, void __user *arg)

    network device ioctl

    :param struct net \*net:
        the applicable net namespace

    :param unsigned int cmd:
        command to issue

    :param void __user \*arg:
        pointer to a struct ifreq in user space



.. _`dev_ioctl.description`:

Description
-----------

Issue ioctl functions to devices. This is normally called by the
user space syscall interfaces but can sometimes be useful for
other purposes. The return value is the return from the syscall if
positive or a negative errno code on error.

