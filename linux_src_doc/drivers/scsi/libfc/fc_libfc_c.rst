.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libfc/fc_libfc.c

.. _`libfc_init`:

libfc_init
==========

.. c:function:: int libfc_init( void)

    Initialize libfc.ko

    :param void:
        no arguments
    :type void: 

.. _`libfc_exit`:

libfc_exit
==========

.. c:function:: void __exit libfc_exit( void)

    Tear down libfc.ko

    :param void:
        no arguments
    :type void: 

.. _`fc_copy_buffer_to_sglist`:

fc_copy_buffer_to_sglist
========================

.. c:function:: u32 fc_copy_buffer_to_sglist(void *buf, size_t len, struct scatterlist *sg, u32 *nents, size_t *offset, u32 *crc)

    This routine copies the data of a buffer into a scatter-gather list (SG list).

    :param buf:
        pointer to the data buffer.
    :type buf: void \*

    :param len:
        the byte-length of the data buffer.
    :type len: size_t

    :param sg:
        pointer to the pointer of the SG list.
    :type sg: struct scatterlist \*

    :param nents:
        pointer to the remaining number of entries in the SG list.
    :type nents: u32 \*

    :param offset:
        pointer to the current offset in the SG list.
    :type offset: size_t \*

    :param crc:
        pointer to the 32-bit crc value.
        If crc is NULL, CRC is not calculated.
    :type crc: u32 \*

.. _`fc_fill_hdr`:

fc_fill_hdr
===========

.. c:function:: void fc_fill_hdr(struct fc_frame *fp, const struct fc_frame *in_fp, enum fc_rctl r_ctl, u32 f_ctl, u16 seq_cnt, u32 parm_offset)

    fill FC header fields based on request

    :param fp:
        reply frame containing header to be filled in
    :type fp: struct fc_frame \*

    :param in_fp:
        request frame containing header to use in filling in reply
    :type in_fp: const struct fc_frame \*

    :param r_ctl:
        R_CTL value for header
    :type r_ctl: enum fc_rctl

    :param f_ctl:
        F_CTL value for header, with 0 pad
    :type f_ctl: u32

    :param seq_cnt:
        sequence count for the header, ignored if frame has a sequence
    :type seq_cnt: u16

    :param parm_offset:
        parameter / offset value
    :type parm_offset: u32

.. _`fc_fill_reply_hdr`:

fc_fill_reply_hdr
=================

.. c:function:: void fc_fill_reply_hdr(struct fc_frame *fp, const struct fc_frame *in_fp, enum fc_rctl r_ctl, u32 parm_offset)

    fill FC reply header fields based on request

    :param fp:
        reply frame containing header to be filled in
    :type fp: struct fc_frame \*

    :param in_fp:
        request frame containing header to use in filling in reply
    :type in_fp: const struct fc_frame \*

    :param r_ctl:
        R_CTL value for reply
    :type r_ctl: enum fc_rctl

    :param parm_offset:
        parameter / offset value
    :type parm_offset: u32

.. _`fc_fc4_conf_lport_params`:

fc_fc4_conf_lport_params
========================

.. c:function:: void fc_fc4_conf_lport_params(struct fc_lport *lport, enum fc_fh_type type)

    Modify "service_params" of specified lport if there is service provider (target provider) registered with libfc for specified "fc_ft_type"

    :param lport:
        Local port which service_params needs to be modified
    :type lport: struct fc_lport \*

    :param type:
        FC-4 type, such as FC_TYPE_FCP
    :type type: enum fc_fh_type

.. _`fc_fc4_register_provider`:

fc_fc4_register_provider
========================

.. c:function:: int fc_fc4_register_provider(enum fc_fh_type type, struct fc4_prov *prov)

    register FC-4 upper-level provider.

    :param type:
        FC-4 type, such as FC_TYPE_FCP
    :type type: enum fc_fh_type

    :param prov:
        structure describing provider including ops vector.
    :type prov: struct fc4_prov \*

.. _`fc_fc4_register_provider.description`:

Description
-----------

Returns 0 on success, negative error otherwise.

.. _`fc_fc4_deregister_provider`:

fc_fc4_deregister_provider
==========================

.. c:function:: void fc_fc4_deregister_provider(enum fc_fh_type type, struct fc4_prov *prov)

    deregister FC-4 upper-level provider.

    :param type:
        FC-4 type, such as FC_TYPE_FCP
    :type type: enum fc_fh_type

    :param prov:
        structure describing provider including ops vector.
    :type prov: struct fc4_prov \*

.. _`fc_fc4_add_lport`:

fc_fc4_add_lport
================

.. c:function:: void fc_fc4_add_lport(struct fc_lport *lport)

    add new local port to list and run notifiers.

    :param lport:
        The new local port.
    :type lport: struct fc_lport \*

.. _`fc_fc4_del_lport`:

fc_fc4_del_lport
================

.. c:function:: void fc_fc4_del_lport(struct fc_lport *lport)

    remove local port from list and run notifiers.

    :param lport:
        The new local port.
    :type lport: struct fc_lport \*

.. This file was automatic generated / don't edit.

