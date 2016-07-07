.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/pcmcia/ds.h

.. _`module_pcmcia_driver`:

module_pcmcia_driver
====================

.. c:function::  module_pcmcia_driver( __pcmcia_driver)

    Helper macro for registering a pcmcia driver

    :param  __pcmcia_driver:
        pcmcia_driver struct

.. _`module_pcmcia_driver.description`:

Description
-----------

Helper macro for pcmcia drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only use
this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ .

.. This file was automatic generated / don't edit.

