.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pcmcia/pcmcia_cis.c

.. _`pccard_read_tuple`:

pccard_read_tuple
=================

.. c:function:: int pccard_read_tuple(struct pcmcia_socket *s, unsigned int function, cisdata_t code, void *parse)

    internal CIS tuple access

    :param s:
        the struct pcmcia_socket where the card is inserted
    :type s: struct pcmcia_socket \*

    :param function:
        the device function we loop for
    :type function: unsigned int

    :param code:
        which CIS code shall we look for?
    :type code: cisdata_t

    :param parse:
        buffer where the tuple shall be parsed (or NULL, if no parse)
    :type parse: void \*

.. _`pccard_read_tuple.description`:

Description
-----------

\ :c:func:`pccard_read_tuple`\  reads out one tuple and attempts to parse it

.. _`pccard_loop_tuple`:

pccard_loop_tuple
=================

.. c:function:: int pccard_loop_tuple(struct pcmcia_socket *s, unsigned int function, cisdata_t code, cisparse_t *parse, void *priv_data, int (*loop_tuple)(tuple_t *tuple, cisparse_t *parse, void *priv_data))

    loop over tuples in the CIS

    :param s:
        the struct pcmcia_socket where the card is inserted
    :type s: struct pcmcia_socket \*

    :param function:
        the device function we loop for
    :type function: unsigned int

    :param code:
        which CIS code shall we look for?
    :type code: cisdata_t

    :param parse:
        buffer where the tuple shall be parsed (or NULL, if no parse)
    :type parse: cisparse_t \*

    :param priv_data:
        private data to be passed to the loop_tuple function.
    :type priv_data: void \*

    :param int (\*loop_tuple)(tuple_t \*tuple, cisparse_t \*parse, void \*priv_data):
        function to call for each CIS entry of type \ ``function``\ . IT
        gets passed the raw tuple, the paresed tuple (if \ ``parse``\  is
        set) and \ ``priv_data``\ .

.. _`pccard_loop_tuple.description`:

Description
-----------

\ :c:func:`pccard_loop_tuple`\  loops over all CIS entries of type \ ``function``\ , and
calls the \ ``loop_tuple``\  function for each entry. If the call to \ ``loop_tuple``\ 
returns 0, the loop exits. Returns 0 on success or errorcode otherwise.

.. _`pcmcia_io_cfg_data_width`:

pcmcia_io_cfg_data_width
========================

.. c:function:: int pcmcia_io_cfg_data_width(unsigned int flags)

    convert cfgtable to data path width parameter

    :param flags:
        *undescribed*
    :type flags: unsigned int

.. _`pcmcia_do_loop_config`:

pcmcia_do_loop_config
=====================

.. c:function:: int pcmcia_do_loop_config(tuple_t *tuple, cisparse_t *parse, void *priv)

    internal helper for \ :c:func:`pcmcia_loop_config`\ 

    :param tuple:
        *undescribed*
    :type tuple: tuple_t \*

    :param parse:
        *undescribed*
    :type parse: cisparse_t \*

    :param priv:
        *undescribed*
    :type priv: void \*

.. _`pcmcia_do_loop_config.description`:

Description
-----------

\ :c:func:`pcmcia_do_loop_config`\  is the internal callback for the call from
\ :c:func:`pcmcia_loop_config`\  to \ :c:func:`pccard_loop_tuple`\ . Data is transferred
by a struct pcmcia_cfg_mem.

.. _`pcmcia_loop_config`:

pcmcia_loop_config
==================

.. c:function:: int pcmcia_loop_config(struct pcmcia_device *p_dev, int (*conf_check)(struct pcmcia_device *p_dev, void *priv_data), void *priv_data)

    loop over configuration options

    :param p_dev:
        the struct pcmcia_device which we need to loop for.
    :type p_dev: struct pcmcia_device \*

    :param int (\*conf_check)(struct pcmcia_device \*p_dev, void \*priv_data):
        function to call for each configuration option.
        It gets passed the struct pcmcia_device and private data
        being passed to \ :c:func:`pcmcia_loop_config`\ 

    :param priv_data:
        private data to be passed to the conf_check function.
    :type priv_data: void \*

.. _`pcmcia_loop_config.description`:

Description
-----------

\ :c:func:`pcmcia_loop_config`\  loops over all configuration options, and calls
the driver-specific \ :c:func:`conf_check`\  for each one, checking whether
it is a valid one. Returns 0 on success or errorcode otherwise.

.. _`pcmcia_do_loop_tuple`:

pcmcia_do_loop_tuple
====================

.. c:function:: int pcmcia_do_loop_tuple(tuple_t *tuple, cisparse_t *parse, void *priv)

    internal helper for \ :c:func:`pcmcia_loop_config`\ 

    :param tuple:
        *undescribed*
    :type tuple: tuple_t \*

    :param parse:
        *undescribed*
    :type parse: cisparse_t \*

    :param priv:
        *undescribed*
    :type priv: void \*

.. _`pcmcia_do_loop_tuple.description`:

Description
-----------

\ :c:func:`pcmcia_do_loop_tuple`\  is the internal callback for the call from
\ :c:func:`pcmcia_loop_tuple`\  to \ :c:func:`pccard_loop_tuple`\ . Data is transferred
by a struct pcmcia_cfg_mem.

.. _`pcmcia_loop_tuple`:

pcmcia_loop_tuple
=================

.. c:function:: int pcmcia_loop_tuple(struct pcmcia_device *p_dev, cisdata_t code, int (*loop_tuple)(struct pcmcia_device *p_dev, tuple_t *tuple, void *priv_data), void *priv_data)

    loop over tuples in the CIS

    :param p_dev:
        the struct pcmcia_device which we need to loop for.
    :type p_dev: struct pcmcia_device \*

    :param code:
        which CIS code shall we look for?
    :type code: cisdata_t

    :param int (\*loop_tuple)(struct pcmcia_device \*p_dev, tuple_t \*tuple, void \*priv_data):
        function to call for each CIS entry of type \ ``function``\ . IT
        gets passed the raw tuple and \ ``priv_data``\ .

    :param priv_data:
        private data to be passed to the loop_tuple function.
    :type priv_data: void \*

.. _`pcmcia_loop_tuple.description`:

Description
-----------

\ :c:func:`pcmcia_loop_tuple`\  loops over all CIS entries of type \ ``function``\ , and
calls the \ ``loop_tuple``\  function for each entry. If the call to \ ``loop_tuple``\ 
returns 0, the loop exits. Returns 0 on success or errorcode otherwise.

.. _`pcmcia_do_get_tuple`:

pcmcia_do_get_tuple
===================

.. c:function:: int pcmcia_do_get_tuple(struct pcmcia_device *p_dev, tuple_t *tuple, void *priv)

    internal helper for \ :c:func:`pcmcia_get_tuple`\ 

    :param p_dev:
        *undescribed*
    :type p_dev: struct pcmcia_device \*

    :param tuple:
        *undescribed*
    :type tuple: tuple_t \*

    :param priv:
        *undescribed*
    :type priv: void \*

.. _`pcmcia_do_get_tuple.description`:

Description
-----------

\ :c:func:`pcmcia_do_get_tuple`\  is the internal callback for the call from
\ :c:func:`pcmcia_get_tuple`\  to \ :c:func:`pcmcia_loop_tuple`\ . As we're only interested in
the first tuple, return 0 unconditionally. Create a memory buffer large
enough to hold the content of the tuple, and fill it with the tuple data.
The caller is responsible to free the buffer.

.. _`pcmcia_get_tuple`:

pcmcia_get_tuple
================

.. c:function:: size_t pcmcia_get_tuple(struct pcmcia_device *p_dev, cisdata_t code, unsigned char **buf)

    get first tuple from CIS

    :param p_dev:
        the struct pcmcia_device which we need to loop for.
    :type p_dev: struct pcmcia_device \*

    :param code:
        which CIS code shall we look for?
    :type code: cisdata_t

    :param buf:
        pointer to store the buffer to.
    :type buf: unsigned char \*\*

.. _`pcmcia_get_tuple.description`:

Description
-----------

\ :c:func:`pcmcia_get_tuple`\  gets the content of the first CIS entry of type \ ``code``\ .
It returns the buffer length (or zero). The caller is responsible to free
the buffer passed in \ ``buf``\ .

.. _`pcmcia_do_get_mac`:

pcmcia_do_get_mac
=================

.. c:function:: int pcmcia_do_get_mac(struct pcmcia_device *p_dev, tuple_t *tuple, void *priv)

    internal helper for \ :c:func:`pcmcia_get_mac_from_cis`\ 

    :param p_dev:
        *undescribed*
    :type p_dev: struct pcmcia_device \*

    :param tuple:
        *undescribed*
    :type tuple: tuple_t \*

    :param priv:
        *undescribed*
    :type priv: void \*

.. _`pcmcia_do_get_mac.description`:

Description
-----------

\ :c:func:`pcmcia_do_get_mac`\  is the internal callback for the call from
\ :c:func:`pcmcia_get_mac_from_cis`\  to \ :c:func:`pcmcia_loop_tuple`\ . We check whether the
tuple contains a proper LAN_NODE_ID of length 6, and copy the data
to struct net_device->dev_addr[i].

.. _`pcmcia_get_mac_from_cis`:

pcmcia_get_mac_from_cis
=======================

.. c:function:: int pcmcia_get_mac_from_cis(struct pcmcia_device *p_dev, struct net_device *dev)

    read out MAC address from CISTPL_FUNCE

    :param p_dev:
        the struct pcmcia_device for which we want the address.
    :type p_dev: struct pcmcia_device \*

    :param dev:
        a properly prepared struct net_device to store the info to.
    :type dev: struct net_device \*

.. _`pcmcia_get_mac_from_cis.description`:

Description
-----------

\ :c:func:`pcmcia_get_mac_from_cis`\  reads out the hardware MAC address from
CISTPL_FUNCE and stores it into struct net_device \*dev->dev_addr which
must be set up properly by the driver (see examples!).

.. This file was automatic generated / don't edit.

