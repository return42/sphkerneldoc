.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/comedi_pcmcia.h

.. _`module_comedi_pcmcia_driver`:

module_comedi_pcmcia_driver
===========================

.. c:function::  module_comedi_pcmcia_driver( __comedi_driver,  __pcmcia_driver)

    Helper macro for registering a comedi PCMCIA driver

    :param  __comedi_driver:
        comedi_driver struct

    :param  __pcmcia_driver:
        pcmcia_driver struct

.. _`module_comedi_pcmcia_driver.description`:

Description
-----------

Helper macro for comedi PCMCIA drivers which do not do anything special
in module init/exit. This eliminates a lot of boilerplate. Each
module may only use this macro once, and calling it replaces
\ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. This file was automatic generated / don't edit.

