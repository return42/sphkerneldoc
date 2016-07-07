.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/s5p-sss.c

.. _`samsung_aes_variant`:

struct samsung_aes_variant
==========================

.. c:type:: struct samsung_aes_variant

    platform specific SSS driver data

.. _`samsung_aes_variant.definition`:

Definition
----------

.. code-block:: c

    struct samsung_aes_variant {
        unsigned int aes_offset;
    }

.. _`samsung_aes_variant.members`:

Members
-------

aes_offset
    AES register offset from SSS module's base.

.. _`samsung_aes_variant.description`:

Description
-----------

Specifies platform specific configuration of SSS module.

.. _`samsung_aes_variant.note`:

Note
----

A structure for driver specific platform data is used for future
expansion of its usage.

.. This file was automatic generated / don't edit.

