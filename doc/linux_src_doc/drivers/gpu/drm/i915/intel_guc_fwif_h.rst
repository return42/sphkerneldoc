.. -*- coding: utf-8; mode: rst -*-

================
intel_guc_fwif.h
================


.. _`guc-firmware-layout`:

GuC Firmware Layout
===================

The GuC firmware layout looks like this::

    +-------------------------------+
    |        guc_css_header         |
    | contains major/minor version  |
    +-------------------------------+
    |             uCode             |
    +-------------------------------+
    |         RSA signature         |
    +-------------------------------+
    |          modulus key          |
    +-------------------------------+
    |          exponent val         |
    +-------------------------------+

The firmware may or may not have modulus key and exponent data. The header,
uCode and RSA signature are must-have components that will be used by driver.
Length of each components, which is all in dwords, can be found in header.
In the case that modulus and exponent are not present in fw, a.k.a truncated
image, the length value still appears in header.

Driver will do some basic fw size validation based on the following rules:

1. Header, uCode and RSA are must-have components.
2. All firmware components, if they present, are in the sequence illustrated
in the layout table above.
3. Length info of each component can be found in header, in dwords.
4. Modulus and exponent key are not required by driver. They may not appear
in fw. So driver will load a truncated firmware in this case.

