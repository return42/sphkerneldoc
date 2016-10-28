.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/speakup/spk_types.h

.. _`module_spk_synth`:

module_spk_synth
================

.. c:function::  module_spk_synth( __spk_synth)

    Helper macro for registering a speakup driver

    :param  __spk_synth:
        spk_synth struct
        Helper macro for speakup drivers which do not do anything special in module
        init/exit. This eliminates a lot of boilerplate. Each module may only
        use this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. This file was automatic generated / don't edit.

