.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/hdac_regmap.c

.. _`snd_hdac_regmap_init`:

snd_hdac_regmap_init
====================

.. c:function:: int snd_hdac_regmap_init(struct hdac_device *codec)

    Initialize regmap for HDA register accesses

    :param struct hdac_device \*codec:
        the codec object

.. _`snd_hdac_regmap_init.description`:

Description
-----------

Returns zero for success or a negative error code.

.. _`snd_hdac_regmap_exit`:

snd_hdac_regmap_exit
====================

.. c:function:: void snd_hdac_regmap_exit(struct hdac_device *codec)

    Release the regmap from HDA codec

    :param struct hdac_device \*codec:
        the codec object

.. _`snd_hdac_regmap_add_vendor_verb`:

snd_hdac_regmap_add_vendor_verb
===============================

.. c:function:: int snd_hdac_regmap_add_vendor_verb(struct hdac_device *codec, unsigned int verb)

    add a vendor-specific verb to regmap

    :param struct hdac_device \*codec:
        the codec object

    :param unsigned int verb:
        verb to allow accessing via regmap

.. _`snd_hdac_regmap_add_vendor_verb.description`:

Description
-----------

Returns zero for success or a negative error code.

.. _`snd_hdac_regmap_write_raw`:

snd_hdac_regmap_write_raw
=========================

.. c:function:: int snd_hdac_regmap_write_raw(struct hdac_device *codec, unsigned int reg, unsigned int val)

    write a pseudo register with power mgmt

    :param struct hdac_device \*codec:
        the codec object

    :param unsigned int reg:
        pseudo register

    :param unsigned int val:
        value to write

.. _`snd_hdac_regmap_write_raw.description`:

Description
-----------

Returns zero if successful or a negative error code.

.. _`snd_hdac_regmap_read_raw`:

snd_hdac_regmap_read_raw
========================

.. c:function:: int snd_hdac_regmap_read_raw(struct hdac_device *codec, unsigned int reg, unsigned int *val)

    read a pseudo register with power mgmt

    :param struct hdac_device \*codec:
        the codec object

    :param unsigned int reg:
        pseudo register

    :param unsigned int \*val:
        pointer to store the read value

.. _`snd_hdac_regmap_read_raw.description`:

Description
-----------

Returns zero if successful or a negative error code.

.. _`snd_hdac_regmap_update_raw`:

snd_hdac_regmap_update_raw
==========================

.. c:function:: int snd_hdac_regmap_update_raw(struct hdac_device *codec, unsigned int reg, unsigned int mask, unsigned int val)

    update a pseudo register with power mgmt

    :param struct hdac_device \*codec:
        the codec object

    :param unsigned int reg:
        pseudo register

    :param unsigned int mask:
        bit mask to udpate

    :param unsigned int val:
        value to update

.. _`snd_hdac_regmap_update_raw.description`:

Description
-----------

Returns zero if successful or a negative error code.

.. This file was automatic generated / don't edit.

