.. -*- coding: utf-8; mode: rst -*-

.. _xref_migrated_docbock:

================================================================================
                                books (htmldocs)
================================================================================

The books are chunked into small *projects*, which can be build and distributed
stand-alone. Cross reference between these *projects* will be ensured by
`intersphinx`_.  The reST source are build from the DocBook-XML sources with the
:ref:`xref_dbtools`.

.. TODO: should be auto generated with the origin title ...

* `kernel-doc HOWTO <../books/kernel-doc-HOWTO/index.html>`_
* `80211 <../books/80211/index.html>`_
* `alsa-driver-api <../books/alsa-driver-api/index.html>`_
* `crypto-API <../books/crypto-API/index.html>`_
* `debugobjects <../books/debugobjects/index.html>`_
* `device-drivers <../books/device-drivers/index.html>`_
* `deviceiobook <../books/deviceiobook/index.html>`_
* `filesytem <../books/filesystems/index.html>`_
* `gadget <../books/gadget/index.html>`_
* `genericirq <../books/genericirq/index.html>`_
* `gpu <../books/gpu/index.html>`_
* `iio <../books/iio/index.html>`_
* `kernel-api <../books/kernel-api/index.html>`_
* `kernel-hacking <../books/kernel-hacking/index.html>`_
* `kernel-locking <../books/kernel-locking/index.html>`_
* `kgdb <../books/kgdb/index.html>`_
* `libata <../books/libata/index.html>`_
* `librs <../books/librs/index.html>`_
* `linux_tv (media) <../books/linux_tv/index.html>`_
* `lsm <../books/lsm/index.html>`_
* `mtdnand <../books/mtdnand/index.html>`_
* `networking <../books/networking/index.html>`_
* `rapidio <../books/rapidio/index.html>`_
* `regulator <../books/regulator/index.html>`_
* `s390-drivers <../books/s390-drivers/index.html>`_
* `scsi <../books/scsi/index.html>`_
* `sh <../books/sh/index.html>`_
* `tracepoint <../books/tracepoint/index.html>`_
* `uio-howto <../books/uio-howto/index.html>`_
* `usb <../books/usb/index.html>`_
* `w1 <../books/w1/index.html>`_
* `writing-an-alsa-driver <../books/writing-an-alsa-driver/index.html>`_
* `writing_musb_glue_layer <../books/writing_musb_glue_layer/index.html>`_
* `writing_usb_driver <../books/writing_usb_driver/index.html>`_
* `z8530book <../books/z8530book/index.html>`_


Reasons to migrate from DocBook
===============================

* The kernel-doc is based on DocBook 4.1 which is incompatible to 5.x. The 4.x
  toolchains are old and less maintained.

* XML markup is hard to integrate in source-code comments.

* XML markup is horrible for authoring and the DocBook markup is to excessive
  for beginners.

Reasons to migrate to reST + Sphinx-Doc
=======================================

* `Sphinx-Doc`_ is widely used and the tools are well maintained. `Sphinx-Doc`_
  is less academical and has down-to-earth answers where DocBook and it's
  toolchains often fails. E.g. sphinx has *built-in* search-page, automatic
  indices, a code highlighter an solution for :ref:`cross_references` and much
  more.

* ASCII markup is already in the source-code comments. reST extends these markup
  ability while existing toolchains can be further used. The ``kernel-doc``
  script needs only a reST output, thats all (see :ref:`xref_kernel-doc`).

* ASCII markups are easy for authoring. reST has a clear syntax definition and
  is the most expressive and expandable ASCII markup.

The Sphinx-Doc generator's approach is complete different to XML applications,
while the reST syntax definition is simple and unambiguously. Coders (the
kernel-doc authors) who gets familiar with reST will love the markup. The
readers appreciate the presentation, build by `Sphinx-Doc`_ . But, compare it by
yourself: DocBook authoring/rendering versus a reST markup with a `Sphinx-Doc`_
toolchain ...

* authoring: origin `DocBook XML books`_ and `reST books`_
* rendering: origin `HTML DocBook books`_ and links above.

.. include:: refs.txt
