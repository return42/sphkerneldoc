.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/cap.c

.. _`tb_find_cap`:

tb_find_cap
===========

.. c:function:: int tb_find_cap(struct tb_port *port, enum tb_cfg_space space, enum tb_cap cap)

    find a capability

    :param struct tb_port \*port:
        *undescribed*

    :param enum tb_cfg_space space:
        *undescribed*

    :param enum tb_cap cap:
        *undescribed*

.. _`tb_find_cap.return`:

Return
------

Returns a positive offset if the capability was found and 0 if not.
Returns an error code on failure.

.. This file was automatic generated / don't edit.

