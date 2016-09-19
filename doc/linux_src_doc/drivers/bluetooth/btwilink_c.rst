.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bluetooth/btwilink.c

.. _`ti_st`:

struct ti_st
============

.. c:type:: struct ti_st

    driver operation structure

.. _`ti_st.definition`:

Definition
----------

.. code-block:: c

    struct ti_st {
        struct hci_dev *hdev;
        char reg_status;
        long (*st_write)(struct sk_buff *);
        struct completion wait_reg_completion;
    }

.. _`ti_st.members`:

Members
-------

hdev
    hci device pointer which binds to bt driver

reg_status
    ST registration callback status

st_write
    write function provided by the ST driver
    to be used by the driver during send_frame.
    \ ``wait_reg_completion``\  - completion sync between ti_st_open
    and st_reg_completion_cb.

wait_reg_completion
    *undescribed*

.. This file was automatic generated / don't edit.

