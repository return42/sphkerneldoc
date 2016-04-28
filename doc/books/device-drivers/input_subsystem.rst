.. -*- coding: utf-8; mode: rst -*-

.. _input_subsystem:

===============
Input Subsystem
===============


Input core
==========


.. toctree::
    :maxdepth: 1

    API-struct-input-value
    API-struct-input-dev
    API-struct-input-handler
    API-struct-input-handle
    API-input-set-events-per-packet
    API-struct-ff-device
    API-input-event
    API-input-inject-event
    API-input-alloc-absinfo
    API-input-grab-device
    API-input-release-device
    API-input-open-device
    API-input-close-device
    API-input-scancode-to-scalar
    API-input-get-keycode
    API-input-set-keycode
    API-input-reset-device
    API-input-allocate-device
    API-devm-input-allocate-device
    API-input-free-device
    API-input-set-capability
    API-input-enable-softrepeat
    API-input-register-device
    API-input-unregister-device
    API-input-register-handler
    API-input-unregister-handler
    API-input-handler-for-each-handle
    API-input-register-handle
    API-input-unregister-handle
    API-input-get-new-minor
    API-input-free-minor
    API-input-ff-upload
    API-input-ff-erase
    API-input-ff-event
    API-input-ff-create
    API-input-ff-destroy
    API-input-ff-create-memless


Multitouch Library
==================


.. toctree::
    :maxdepth: 1

    API-struct-input-mt-slot
    API-struct-input-mt
    API-struct-input-mt-pos
    API-input-mt-init-slots
    API-input-mt-destroy-slots
    API-input-mt-report-slot-state
    API-input-mt-report-finger-count
    API-input-mt-report-pointer-emulation
    API-input-mt-drop-unused
    API-input-mt-sync-frame
    API-input-mt-assign-slots
    API-input-mt-get-slot-by-key


Polled input devices
====================


.. toctree::
    :maxdepth: 1

    API-struct-input-polled-dev
    API-input-allocate-polled-device
    API-devm-input-allocate-polled-device
    API-input-free-polled-device
    API-input-register-polled-device
    API-input-unregister-polled-device


Matrix keyboards/keypads
========================


.. toctree::
    :maxdepth: 1

    API-struct-matrix-keymap-data
    API-struct-matrix-keypad-platform-data
    API-matrix-keypad-parse-of-params


Sparse keymap support
=====================


.. toctree::
    :maxdepth: 1

    API-struct-key-entry
    API-sparse-keymap-entry-from-scancode
    API-sparse-keymap-entry-from-keycode
    API-sparse-keymap-setup
    API-sparse-keymap-free
    API-sparse-keymap-report-entry
    API-sparse-keymap-report-event




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
