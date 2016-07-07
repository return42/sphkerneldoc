.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/drx39xyj/drx_driver.h

.. _`drxu_code_action`:

enum drxu_code_action
=====================

.. c:type:: enum drxu_code_action

    indicate if firmware has to be uploaded or verified.

.. _`drxu_code_action.definition`:

Definition
----------

.. code-block:: c

    enum drxu_code_action {
        UCODE_UPLOAD,
        UCODE_VERIFY
    };

.. _`drxu_code_action.constants`:

Constants
---------

UCODE_UPLOAD
    Upload the microcode image to device

UCODE_VERIFY
    Compare microcode image with code on device

.. _`drxu_code_info`:

struct drxu_code_info
=====================

.. c:type:: struct drxu_code_info


.. _`drxu_code_info.definition`:

Definition
----------

.. code-block:: c

    struct drxu_code_info {
        char *mc_file;
    }

.. _`drxu_code_info.members`:

Members
-------

mc_file
    microcode file name

.. _`drxu_code_info.description`:

Description
-----------

Used by DRX_CTRL_LOAD_UCODE and DRX_CTRL_VERIFY_UCODE

.. This file was automatic generated / don't edit.

