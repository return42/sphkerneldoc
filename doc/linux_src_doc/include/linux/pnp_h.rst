.. -*- coding: utf-8; mode: rst -*-

=====
pnp.h
=====


.. _`module_pnp_driver`:

module_pnp_driver
=================

.. c:function:: module_pnp_driver ( __pnp_driver)

    Helper macro for registering a PnP driver

    :param __pnp_driver:
        pnp_driver struct



.. _`module_pnp_driver.description`:

Description
-----------

Helper macro for PnP drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces :c:func:`module_init` and :c:func:`module_exit`

