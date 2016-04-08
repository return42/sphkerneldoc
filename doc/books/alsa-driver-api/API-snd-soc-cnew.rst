
.. _API-snd-soc-cnew:

============
snd_soc_cnew
============

*man snd_soc_cnew(9)*

*4.6.0-rc1*

create new control


Synopsis
========

.. c:function:: struct snd_kcontrol ⋆ snd_soc_cnew( const struct snd_kcontrol_new * _template, void * data, const char * long_name, const char * prefix )

Arguments
=========

``_template``
    control template

``data``
    control private data

``long_name``
    control long name

``prefix``
    control name prefix


Description
===========

Create a new mixer control from a template control.

Returns 0 for success, else error.
