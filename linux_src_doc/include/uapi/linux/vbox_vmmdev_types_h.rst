.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/vbox_vmmdev_types.h

.. _`vmmdev_hgcm_pagelist`:

struct vmmdev_hgcm_pagelist
===========================

.. c:type:: struct vmmdev_hgcm_pagelist

    VMMDEV_HGCM_PARM_TYPE_PAGELIST parameters point to this structure to actually describe the buffer.

.. _`vmmdev_hgcm_pagelist.definition`:

Definition
----------

.. code-block:: c

    struct vmmdev_hgcm_pagelist {
        __u32 flags;
        __u16 offset_first_page;
        __u16 page_count;
        __u64 pages[1];
    }

.. _`vmmdev_hgcm_pagelist.members`:

Members
-------

flags
    *undescribed*

offset_first_page
    *undescribed*

page_count
    *undescribed*

pages
    *undescribed*

.. This file was automatic generated / don't edit.

