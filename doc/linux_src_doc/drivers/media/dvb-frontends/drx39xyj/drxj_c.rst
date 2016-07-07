.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/drx39xyj/drxj.c

.. _`drxj_16to8`:

DRXJ_16TO8
==========

.. c:function::  DRXJ_16TO8( x)

    Block writes speed up I2C traffic between host and demod. The macro takes care of the required byte order in a 16 bits word. x -> lowbyte(x), highbyte(x)

    :param  x:
        *undescribed*

.. _`drxj_8to16`:

DRXJ_8TO16
==========

.. c:function::  DRXJ_8TO16( x)

    Block read speed up I2C traffic between host and demod. The macro takes care of the required byte order in a 16 bits word.

    :param  x:
        *undescribed*

.. _`drxu_code_block_hdr`:

struct drxu_code_block_hdr
==========================

.. c:type:: struct drxu_code_block_hdr

    Structure of the microcode block headers

.. _`drxu_code_block_hdr.definition`:

Definition
----------

.. code-block:: c

    struct drxu_code_block_hdr {
        u32 addr;
        u16 size;
        u16 flags;
        u16 CRC;
    }

.. _`drxu_code_block_hdr.members`:

Members
-------

addr
    Destination address of the data in this block

size
    Size of the block data following this header counted in
    16 bits words

flags
    *undescribed*

CRC
    CRC value of the data block, only valid if CRC flag is
    set.

.. _`drx_u_code_compute_crc`:

drx_u_code_compute_crc
======================

.. c:function:: u16 drx_u_code_compute_crc(u8 *block_data, u16 nr_words)

    Compute CRC of block of microcode data.

    :param u8 \*block_data:
        Pointer to microcode data.

    :param u16 nr_words:
        Size of microcode block (number of 16 bits words).

.. _`drx_u_code_compute_crc.description`:

Description
-----------

returns The computed CRC residue.

.. _`drx_check_firmware`:

drx_check_firmware
==================

.. c:function:: int drx_check_firmware(struct drx_demod_instance *demod, u8 *mc_data, unsigned size)

    checks if the loaded firmware is valid

    :param struct drx_demod_instance \*demod:
        demod structure

    :param u8 \*mc_data:
        pointer to the start of the firmware

    :param unsigned size:
        firmware size

.. _`drx_ctrl_u_code`:

drx_ctrl_u_code
===============

.. c:function:: int drx_ctrl_u_code(struct drx_demod_instance *demod, struct drxu_code_info *mc_info, enum drxu_code_action action)

    Handle microcode upload or verify.

    :param struct drx_demod_instance \*demod:
        *undescribed*

    :param struct drxu_code_info \*mc_info:
        Pointer to information about microcode data.

    :param enum drxu_code_action action:
        Either UCODE_UPLOAD or UCODE_VERIFY

.. _`drx_ctrl_u_code.this-function-returns`:

This function returns
---------------------

0:
- In case of UCODE_UPLOAD: code is successfully uploaded.
- In case of UCODE_VERIFY: image on device is equal to
image provided to this control function.
-EIO:
- In case of UCODE_UPLOAD: I2C error.
- In case of UCODE_VERIFY: I2C error or image on device
is not equal to image provided to this control function.
-EINVAL:
- Invalid arguments.
- Provided image is corrupt

.. This file was automatic generated / don't edit.

