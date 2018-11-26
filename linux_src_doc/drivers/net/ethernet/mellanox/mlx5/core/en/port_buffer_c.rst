.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/mellanox/mlx5/core/en/port_buffer.c

.. _`update_buffer_lossy`:

update_buffer_lossy
===================

.. c:function:: int update_buffer_lossy(unsigned int mtu, u8 pfc_en, u8 *buffer, u32 xoff, struct mlx5e_port_buffer *port_buffer, bool *change)

    :param mtu:
        *undescribed*
    :type mtu: unsigned int

    :param pfc_en:
        *undescribed*
    :type pfc_en: u8

    :param buffer:
        *undescribed*
    :type buffer: u8 \*

    :param xoff:
        *undescribed*
    :type xoff: u32

    :param port_buffer:
        *undescribed*
    :type port_buffer: struct mlx5e_port_buffer \*

    :param change:
        *undescribed*
    :type change: bool \*

.. _`update_buffer_lossy.mtu`:

mtu
---

device's MTU

.. _`update_buffer_lossy.pfc_en`:

pfc_en
------

<input> current pfc configuration

.. _`update_buffer_lossy.buffer`:

buffer
------

<input> current prio to buffer mapping

.. _`update_buffer_lossy.xoff`:

xoff
----

<input> xoff value

.. _`update_buffer_lossy.port_buffer`:

port_buffer
-----------

<output> port receive buffer configuration

.. _`update_buffer_lossy.change`:

change
------

<output>

Update buffer configuration based on pfc configuraiton and priority
to buffer mapping.
Buffer's lossy bit is changed to:
lossless if there is at least one PFC enabled priority mapped to this buffer
lossy if all priorities mapped to this buffer are PFC disabled

.. _`update_buffer_lossy.return`:

Return
------

Return 0 if no error.
Set change to true if buffer configuration is modified.

.. This file was automatic generated / don't edit.

