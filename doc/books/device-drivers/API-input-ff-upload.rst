
.. _API-input-ff-upload:

===============
input_ff_upload
===============

*man input_ff_upload(9)*

*4.6.0-rc1*

upload effect into force-feedback device


Synopsis
========

.. c:function:: int input_ff_upload( struct input_dev * dev, struct ff_effect * effect, struct file * file )

Arguments
=========

``dev``
    input device

``effect``
    effect to be uploaded

``file``
    owner of the effect
