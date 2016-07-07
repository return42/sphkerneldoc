.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/fc_encode.h

.. _`fc_fill_fc_hdr`:

fc_fill_fc_hdr
==============

.. c:function:: void fc_fill_fc_hdr(struct fc_frame *fp, enum fc_rctl r_ctl, u32 did, u32 sid, enum fc_fh_type type, u32 f_ctl, u32 parm_offset)

    :param struct fc_frame \*fp:
        *undescribed*

    :param enum fc_rctl r_ctl:
        *undescribed*

    :param u32 did:
        *undescribed*

    :param u32 sid:
        *undescribed*

    :param enum fc_fh_type type:
        *undescribed*

    :param u32 f_ctl:
        *undescribed*

    :param u32 parm_offset:
        *undescribed*

.. _`fc_adisc_fill`:

fc_adisc_fill
=============

.. c:function:: void fc_adisc_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in adisc request frame

    :param struct fc_lport \*lport:
        local port.

    :param struct fc_frame \*fp:
        fc frame where payload will be placed.

.. _`fc_ct_hdr_fill`:

fc_ct_hdr_fill
==============

.. c:function:: struct fc_ct_req *fc_ct_hdr_fill(const struct fc_frame *fp, unsigned int op, size_t req_size, enum fc_ct_fs_type fs_type, u8 subtype)

    fills ct header and reset ct payload returns pointer to ct request.

    :param const struct fc_frame \*fp:
        *undescribed*

    :param unsigned int op:
        *undescribed*

    :param size_t req_size:
        *undescribed*

    :param enum fc_ct_fs_type fs_type:
        *undescribed*

    :param u8 subtype:
        *undescribed*

.. _`fc_ct_ns_fill`:

fc_ct_ns_fill
=============

.. c:function:: int fc_ct_ns_fill(struct fc_lport *lport, u32 fc_id, struct fc_frame *fp, unsigned int op, enum fc_rctl *r_ctl, enum fc_fh_type *fh_type)

    Fill in a name service request frame

    :param struct fc_lport \*lport:
        local port.

    :param u32 fc_id:
        FC_ID of non-destination rport for GPN_ID and similar inquiries.

    :param struct fc_frame \*fp:
        frame to contain payload.

    :param unsigned int op:
        CT opcode.

    :param enum fc_rctl \*r_ctl:
        pointer to FC header R_CTL.

    :param enum fc_fh_type \*fh_type:
        pointer to FC-4 type.

.. _`fc_ct_ms_fill`:

fc_ct_ms_fill
=============

.. c:function:: int fc_ct_ms_fill(struct fc_lport *lport, u32 fc_id, struct fc_frame *fp, unsigned int op, enum fc_rctl *r_ctl, enum fc_fh_type *fh_type)

    Fill in a mgmt service request frame

    :param struct fc_lport \*lport:
        local port.

    :param u32 fc_id:
        FC_ID of non-destination rport for GPN_ID and similar inquiries.

    :param struct fc_frame \*fp:
        frame to contain payload.

    :param unsigned int op:
        CT opcode.

    :param enum fc_rctl \*r_ctl:
        pointer to FC header R_CTL.

    :param enum fc_fh_type \*fh_type:
        pointer to FC-4 type.

.. _`fc_ct_fill`:

fc_ct_fill
==========

.. c:function:: int fc_ct_fill(struct fc_lport *lport, u32 fc_id, struct fc_frame *fp, unsigned int op, enum fc_rctl *r_ctl, enum fc_fh_type *fh_type, u32 *did)

    Fill in a common transport service request frame

    :param struct fc_lport \*lport:
        local port.

    :param u32 fc_id:
        FC_ID of non-destination rport for GPN_ID and similar inquiries.

    :param struct fc_frame \*fp:
        frame to contain payload.

    :param unsigned int op:
        CT opcode.

    :param enum fc_rctl \*r_ctl:
        pointer to FC header R_CTL.

    :param enum fc_fh_type \*fh_type:
        pointer to FC-4 type.

    :param u32 \*did:
        *undescribed*

.. _`fc_plogi_fill`:

fc_plogi_fill
=============

.. c:function:: void fc_plogi_fill(struct fc_lport *lport, struct fc_frame *fp, unsigned int op)

    Fill in plogi request frame

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

    :param unsigned int op:
        *undescribed*

.. _`fc_flogi_fill`:

fc_flogi_fill
=============

.. c:function:: void fc_flogi_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in a flogi request frame.

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

.. _`fc_fdisc_fill`:

fc_fdisc_fill
=============

.. c:function:: void fc_fdisc_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in a fdisc request frame.

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

.. _`fc_logo_fill`:

fc_logo_fill
============

.. c:function:: void fc_logo_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in a logo request frame.

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

.. _`fc_rtv_fill`:

fc_rtv_fill
===========

.. c:function:: void fc_rtv_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in RTV (read timeout value) request frame.

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

.. _`fc_rec_fill`:

fc_rec_fill
===========

.. c:function:: void fc_rec_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in rec request frame

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

.. _`fc_prli_fill`:

fc_prli_fill
============

.. c:function:: void fc_prli_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in prli request frame

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

.. _`fc_scr_fill`:

fc_scr_fill
===========

.. c:function:: void fc_scr_fill(struct fc_lport *lport, struct fc_frame *fp)

    Fill in a scr request frame.

    :param struct fc_lport \*lport:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

.. _`fc_els_fill`:

fc_els_fill
===========

.. c:function:: int fc_els_fill(struct fc_lport *lport, u32 did, struct fc_frame *fp, unsigned int op, enum fc_rctl *r_ctl, enum fc_fh_type *fh_type)

    Fill in an ELS  request frame

    :param struct fc_lport \*lport:
        *undescribed*

    :param u32 did:
        *undescribed*

    :param struct fc_frame \*fp:
        *undescribed*

    :param unsigned int op:
        *undescribed*

    :param enum fc_rctl \*r_ctl:
        *undescribed*

    :param enum fc_fh_type \*fh_type:
        *undescribed*

.. This file was automatic generated / don't edit.

