.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/pcie.c

.. _`brcmf_pcie_dhi_ringinfo`:

struct brcmf_pcie_dhi_ringinfo
==============================

.. c:type:: struct brcmf_pcie_dhi_ringinfo

    dongle/host interface shared ring info

.. _`brcmf_pcie_dhi_ringinfo.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_pcie_dhi_ringinfo {
        __le32 ringmem;
        __le32 h2d_w_idx_ptr;
        __le32 h2d_r_idx_ptr;
        __le32 d2h_w_idx_ptr;
        __le32 d2h_r_idx_ptr;
        struct msgbuf_buf_addr h2d_w_idx_hostaddr;
        struct msgbuf_buf_addr h2d_r_idx_hostaddr;
        struct msgbuf_buf_addr d2h_w_idx_hostaddr;
        struct msgbuf_buf_addr d2h_r_idx_hostaddr;
        __le16 max_flowrings;
        __le16 max_submissionrings;
        __le16 max_completionrings;
    }

.. _`brcmf_pcie_dhi_ringinfo.members`:

Members
-------

ringmem
    dongle memory pointer to ring memory location

h2d_w_idx_ptr
    h2d ring write indices dongle memory pointers

h2d_r_idx_ptr
    h2d ring read indices dongle memory pointers

d2h_w_idx_ptr
    d2h ring write indices dongle memory pointers

d2h_r_idx_ptr
    d2h ring read indices dongle memory pointers

h2d_w_idx_hostaddr
    h2d ring write indices host memory pointers

h2d_r_idx_hostaddr
    h2d ring read indices host memory pointers

d2h_w_idx_hostaddr
    d2h ring write indices host memory pointers

d2h_r_idx_hostaddr
    d2h ring reaD indices host memory pointers

max_flowrings
    maximum number of tx flow rings supported.

max_submissionrings
    maximum number of submission rings(h2d) supported.

max_completionrings
    maximum number of completion rings(d2h) supported.

.. This file was automatic generated / don't edit.

