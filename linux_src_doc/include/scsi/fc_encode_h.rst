.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/fc_encode.h

.. _`fc_fill_fc_hdr`:

fc_fill_fc_hdr
==============

.. c:function:: void fc_fill_fc_hdr(struct fc_frame *fp, enum fc_rctl r_ctl, u32 did, u32 sid, enum fc_fh_type type, u32 f_ctl, u32 parm_offset)

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

    :param r_ctl:
        *undescribed*
    :type r_ctl: enum fc_rctl

    :param did:
        *undescribed*
    :type did: u32

    :param sid:
        *undescribed*
    :type sid: u32

    :param type:
        *undescribed*
    :type type: enum fc_fh_type

    :param f_ctl:
        *undescribed*
    :type f_ctl: u32

    :param parm_offset:
        *undescribed*
    :type parm_offset: u32

.. _`fc_adisc_fill`:

fc_adisc_fill
=============

.. c:function:: void fc_adisc_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in adisc request frame

    :param lport:
        local port.
    :type lport: struct fc_lport \*

    :param fp:
        fc frame where payload will be placed.
    :type fp: struct fc_frame \*

.. _`fc_ct_hdr_fill`:

fc_ct_hdr_fill
==============

.. c:function:: struct fc_ct_req *fc_ct_hdr_fill(const struct fc_frame *fp, unsigned int op, size_t req_size, enum fc_ct_fs_type fs_type, u8 subtype)

    fills ct header and reset ct payload returns pointer to ct request.

    :param fp:
        *undescribed*
    :type fp: const struct fc_frame \*

    :param op:
        *undescribed*
    :type op: unsigned int

    :param req_size:
        *undescribed*
    :type req_size: size_t

    :param fs_type:
        *undescribed*
    :type fs_type: enum fc_ct_fs_type

    :param subtype:
        *undescribed*
    :type subtype: u8

.. _`fc_ct_ns_fill`:

fc_ct_ns_fill
=============

.. c:function:: int fc_ct_ns_fill(struct fc_lport *lport, u32 fc_id, struct fc_frame *fp, unsigned int op, enum fc_rctl *r_ctl, enum fc_fh_type *fh_type)

    Fill in a name service request frame

    :param lport:
        local port.
    :type lport: struct fc_lport \*

    :param fc_id:
        FC_ID of non-destination rport for GPN_ID and similar inquiries.
    :type fc_id: u32

    :param fp:
        frame to contain payload.
    :type fp: struct fc_frame \*

    :param op:
        CT opcode.
    :type op: unsigned int

    :param r_ctl:
        pointer to FC header R_CTL.
    :type r_ctl: enum fc_rctl \*

    :param fh_type:
        pointer to FC-4 type.
    :type fh_type: enum fc_fh_type \*

.. _`fc_ct_ms_fill`:

fc_ct_ms_fill
=============

.. c:function:: int fc_ct_ms_fill(struct fc_lport *lport, u32 fc_id, struct fc_frame *fp, unsigned int op, enum fc_rctl *r_ctl, enum fc_fh_type *fh_type)

    Fill in a mgmt service request frame

    :param lport:
        local port.
    :type lport: struct fc_lport \*

    :param fc_id:
        FC_ID of non-destination rport for GPN_ID and similar inquiries.
    :type fc_id: u32

    :param fp:
        frame to contain payload.
    :type fp: struct fc_frame \*

    :param op:
        CT opcode.
    :type op: unsigned int

    :param r_ctl:
        pointer to FC header R_CTL.
    :type r_ctl: enum fc_rctl \*

    :param fh_type:
        pointer to FC-4 type.
    :type fh_type: enum fc_fh_type \*

.. _`fc_ct_fill`:

fc_ct_fill
==========

.. c:function:: int fc_ct_fill(struct fc_lport *lport, u32 fc_id, struct fc_frame *fp, unsigned int op, enum fc_rctl *r_ctl, enum fc_fh_type *fh_type, u32 *did)

    Fill in a common transport service request frame

    :param lport:
        local port.
    :type lport: struct fc_lport \*

    :param fc_id:
        FC_ID of non-destination rport for GPN_ID and similar inquiries.
    :type fc_id: u32

    :param fp:
        frame to contain payload.
    :type fp: struct fc_frame \*

    :param op:
        CT opcode.
    :type op: unsigned int

    :param r_ctl:
        pointer to FC header R_CTL.
    :type r_ctl: enum fc_rctl \*

    :param fh_type:
        pointer to FC-4 type.
    :type fh_type: enum fc_fh_type \*

    :param did:
        *undescribed*
    :type did: u32 \*

.. _`fc_plogi_fill`:

fc_plogi_fill
=============

.. c:function:: void fc_plogi_fill(struct fc_lport *lport, struct fc_frame *fp, unsigned int op)

    Fill in plogi request frame

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

    :param op:
        *undescribed*
    :type op: unsigned int

.. _`fc_flogi_fill`:

fc_flogi_fill
=============

.. c:function:: void fc_flogi_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in a flogi request frame.

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

.. _`fc_fdisc_fill`:

fc_fdisc_fill
=============

.. c:function:: void fc_fdisc_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in a fdisc request frame.

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

.. _`fc_logo_fill`:

fc_logo_fill
============

.. c:function:: void fc_logo_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in a logo request frame.

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

.. _`fc_rtv_fill`:

fc_rtv_fill
===========

.. c:function:: void fc_rtv_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in RTV (read timeout value) request frame.

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

.. _`fc_rec_fill`:

fc_rec_fill
===========

.. c:function:: void fc_rec_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in rec request frame

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

.. _`fc_prli_fill`:

fc_prli_fill
============

.. c:function:: void fc_prli_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in prli request frame

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

.. _`fc_scr_fill`:

fc_scr_fill
===========

.. c:function:: void fc_scr_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in a scr request frame.

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

.. _`fc_els_fill`:

fc_els_fill
===========

.. c:function:: int fc_els_fill(struct fc_lport *lport, u32 did, struct fc_frame *fp, unsigned int op, enum fc_rctl *r_ctl, enum fc_fh_type *fh_type)

    Fill in an ELS  request frame

    :param lport:
        *undescribed*
    :type lport: struct fc_lport \*

    :param did:
        *undescribed*
    :type did: u32

    :param fp:
        *undescribed*
    :type fp: struct fc_frame \*

    :param op:
        *undescribed*
    :type op: unsigned int

    :param r_ctl:
        *undescribed*
    :type r_ctl: enum fc_rctl \*

    :param fh_type:
        *undescribed*
    :type fh_type: enum fc_fh_type \*

.. This file was automatic generated / don't edit.

