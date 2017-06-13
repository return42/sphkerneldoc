.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt


================================================================================
                        Linux Kernel's documentation POC
================================================================================

This is a *POC* to demonstrate how a *straight forward* documentation build
might look like.  At this time, not all of this POC is a part of the Linux
kernel source tree. If you wan't to read more about reST, Sphinx and this POC
jump to:

.. toctree::
   :maxdepth: 1

   poc_sphkerneldoc/index

Mostly you want to jump to the kernel documentation build by this POC.

While the documentation build of kernel's sources is just one monolith (`ref
<http://static.lwn.net/kerneldoc/>`__), this POC builds documentation separated
into books:

.. toctree::
   :maxdepth: 1

   docs

With the :ref:`kernel-autodoc <linuxdoc:kernel-autodoc>` tool from the
:ref:`LinuxDoc project <linuxdoc:linuxdoc>` the *kernel-doc* comments from
Kernel's source code are parsed and converted to reST.  Be aware, that this is
in a experimental state, see :ref:`xref_linux_src_doc`.

* `Linux kernel source <linux_src_doc/index.html>`_


