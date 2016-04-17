.. -*- coding: utf-8; mode: rst -*-

=========
s5p-sss.c
=========


.. _`samsung_aes_variant`:

struct samsung_aes_variant
==========================

.. c:type:: samsung_aes_variant

    platform specific SSS driver data


.. _`samsung_aes_variant.definition`:

Definition
----------

.. code-block:: c

  struct samsung_aes_variant {
    bool has_hash_irq;
    unsigned int aes_offset;
  };


.. _`samsung_aes_variant.members`:

Members
-------

:``has_hash_irq``:
    true if SSS module uses hash interrupt, false otherwise

:``aes_offset``:
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

