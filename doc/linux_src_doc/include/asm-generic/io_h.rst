.. -*- coding: utf-8; mode: rst -*-

====
io.h
====


.. _`ioremap---and-ioremap_----variants`:

ioremap() and ioremap_*() variants
==================================

If you have an IOMMU your architecture is expected to have both :c:func:`ioremap`
and :c:func:`iounmap` implemented otherwise the asm-generic helpers will provide a
direct mapping.

There are ioremap\_\*() call variants, if you have no IOMMU we naturally will
default to direct mapping for all of them, you can override these defaults.
If you have an IOMMU you are highly encouraged to provide your own
ioremap variant implementation as there currently is no safe architecture
agnostic default. To avoid possible improper behaviour default asm-generic
ioremap\_\*() variants all return NULL when an IOMMU is available. If you've
defined your own ioremap\_\*() variant you must then declare your own
ioremap\_\*() variant as defined to itself to avoid the default NULL return.

