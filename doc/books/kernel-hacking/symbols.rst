
.. _symbols:

=======
Symbols
=======

Within the kernel proper, the normal linking rules apply (ie. unless a symbol is declared to be file scope with the ``static`` keyword, it can be used anywhere in the kernel).
However, for modules, a special exported symbol table is kept which limits the entry points to the kernel proper. Modules can also export symbols.


.. _sym-exportsymbols:

EXPORT_SYMBOL() include/linux/export.h
======================================

This is the classic method of exporting a symbol: dynamically loaded modules will be able to use the symbol as normal.


.. _sym-exportsymbols-gpl:

EXPORT_SYMBOL_GPL() include/linux/export.h
==========================================

Similar to ``EXPORT_SYMBOL()`` except that the symbols exported by ``EXPORT_SYMBOL_GPL()`` can only be seen by modules with a ``MODULE_LICENSE()`` that specifies a GPL compatible
license. It implies that the function is considered an internal implementation issue, and not really an interface. Some maintainers and developers may however require
EXPORT_SYMBOL_GPL() when adding any new APIs or functionality.
