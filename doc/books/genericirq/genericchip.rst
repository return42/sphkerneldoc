
.. _genericchip:

======================
Generic interrupt chip
======================

To avoid copies of identical implementations of IRQ chips the core provides a configurable generic interrupt chip implementation. Developers should check carefully whether the
generic chip fits their needs before implementing the same functionality slightly differently themselves.


.. toctree::
    :maxdepth: 1

    API-irq-gc-mask-set-bit
    API-irq-gc-mask-clr-bit
    API-irq-gc-ack-set-bit
    API-irq-alloc-generic-chip
    API-irq-alloc-domain-generic-chips
    API-irq-get-domain-generic-chip
    API-irq-setup-generic-chip
    API-irq-setup-alt-chip
    API-irq-remove-generic-chip
