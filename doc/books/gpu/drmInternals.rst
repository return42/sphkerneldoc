.. -*- coding: utf-8; mode: rst -*-

.. _drmInternals:

=============
DRM Internals
=============

This chapter documents DRM internals relevant to driver authors and
developers working to add support for the latest features to existing
drivers.

First, we go over some typical driver initialization requirements, like
setting up command buffers, creating an initial output configuration,
and initializing core services. Subsequent sections cover core internals
in more detail, providing implementation notes and examples.

The DRM layer provides several services to graphics drivers, many of
them driven by the application interfaces it provides through libdrm,
the library that wraps most of the DRM ioctls. These include vblank
event handling, memory management, output management, framebuffer
management, command submission & fencing, suspend/resume support, and
DMA services.


Driver Initialization
=====================

At the core of every DRM driver is a ``drm_driver`` structure. Drivers
typically statically initialize a drm_driver structure, and then pass
it to ``drm_dev_alloc()`` to allocate a device instance. After the
device instance is fully initialized it can be registered (which makes
it accessible from userspace) using ``drm_dev_register()``.

The ``drm_driver`` structure contains static information that describes
the driver and features it supports, and pointers to methods that the
DRM core will call to implement the DRM API. We will first go through
the ``drm_driver`` static information fields, and will then describe
individual operations in details as they get used in later sections.


Driver Information
------------------


Driver Features
+++++++++++++++

Drivers inform the DRM core about their requirements and supported
features by setting appropriate flags in the ``driver_features`` field.
Since those flags influence the DRM core behaviour since registration
time, most of them must be set to registering the ``drm_driver``
instance.


.. code-block:: c

    u32 driver_features;

DRIVER_USE_AGP
    Driver uses AGP interface, the DRM core will manage AGP resources.

DRIVER_REQUIRE_AGP
    Driver needs AGP interface to function. AGP initialization failure
    will become a fatal error.

DRIVER_PCI_DMA
    Driver is capable of PCI DMA, mapping of PCI DMA buffers to
    userspace will be enabled. Deprecated.

DRIVER_SG
    Driver can perform scatter/gather DMA, allocation and mapping of
    scatter/gather buffers will be enabled. Deprecated.

DRIVER_HAVE_DMA
    Driver supports DMA, the userspace DMA API will be supported.
    Deprecated.

DRIVER_HAVE_IRQ; DRIVER_IRQ_SHARED
    DRIVER_HAVE_IRQ indicates whether the driver has an IRQ handler
    managed by the DRM Core. The core will support simple IRQ handler
    installation when the flag is set. The installation process is
    described in :ref:`drm-irq-registration`.

    DRIVER_IRQ_SHARED indicates whether the device & handler support
    shared IRQs (note that this is required of PCI drivers).

DRIVER_GEM
    Driver use the GEM memory manager.

DRIVER_MODESET
    Driver supports mode setting interfaces (KMS).

DRIVER_PRIME
    Driver implements DRM PRIME buffer sharing.

DRIVER_RENDER
    Driver supports dedicated render nodes.

DRIVER_ATOMIC
    Driver supports atomic properties. In this case the driver must
    implement appropriate obj->atomic_get_property() vfuncs for any
    modeset objects with driver specific properties.


Major, Minor and Patchlevel
+++++++++++++++++++++++++++


.. code-block:: c

    int major;
    int minor;
    int patchlevel;

The DRM core identifies driver versions by a major, minor and patch
level triplet. The information is printed to the kernel log at
initialization time and passed to userspace through the
DRM_IOCTL_VERSION ioctl.

The major and minor numbers are also used to verify the requested driver
API version passed to DRM_IOCTL_SET_VERSION. When the driver API
changes between minor versions, applications can call
DRM_IOCTL_SET_VERSION to select a specific version of the API. If the
requested major isn't equal to the driver major, or the requested minor
is larger than the driver minor, the DRM_IOCTL_SET_VERSION call will
return an error. Otherwise the driver's set_version() method will be
called with the requested version.


Name, Description and Date
++++++++++++++++++++++++++


.. code-block:: c

    char *name;
    char *desc;
    char *date;

The driver name is printed to the kernel log at initialization time,
used for IRQ registration and passed to userspace through
DRM_IOCTL_VERSION.

The driver description is a purely informative string passed to
userspace through the DRM_IOCTL_VERSION ioctl and otherwise unused by
the kernel.

The driver date, formatted as YYYYMMDD, is meant to identify the date of
the latest modification to the driver. However, as most drivers fail to
update it, its value is mostly useless. The DRM core prints it to the
kernel log at initialization time and passes it to userspace through the
DRM_IOCTL_VERSION ioctl.


Device Instance and Driver Handling
-----------------------------------

A device instance for a drm driver is represented by struct
``drm_device``. This is allocated with ``drm_dev_alloc``, usually from
bus-specific ->``probe`` callbacks implemented by the driver. The driver
then needs to initialize all the various subsystems for the drm device
like memory management, vblank handling, modesetting support and intial
output configuration plus obviously initialize all the corresponding
hardware bits. An important part of this is also calling
``drm_dev_set_unique`` to set the userspace-visible unique name of this
device instance. Finally when everything is up and running and ready for
userspace the device instance can be published using
``drm_dev_register``.

There is also deprecated support for initalizing device instances using
bus-specific helpers and the ->``load`` callback. But due to
backwards-compatibility needs the device instance have to be published
too early, which requires unpretty global locking to make safe and is
therefore only support for existing drivers not yet converted to the new
scheme.

When cleaning up a device instance everything needs to be done in
reverse: First unpublish the device instance with
``drm_dev_unregister``. Then clean up any other resources allocated at
device initialization and drop the driver's reference to ``drm_device``
using ``drm_dev_unref``.

Note that the lifetime rules for ``drm_device`` instance has still a lot
of historical baggage. Hence use the reference counting provided by
``drm_dev_ref`` and ``drm_dev_unref`` only carefully.

Also note that embedding of ``drm_device`` is currently not (yet)
supported (but it would be easy to add). Drivers can store
driver-private data in the dev_priv field of ``drm_device``.


.. toctree::
    :maxdepth: 1

    API-drm-put-dev
    API-drm-dev-alloc
    API-drm-dev-ref
    API-drm-dev-unref
    API-drm-dev-register
    API-drm-dev-unregister
    API-drm-dev-set-unique


Driver Load
-----------


.. _drm-irq-registration:

IRQ Registration
++++++++++++++++

The DRM core tries to facilitate IRQ handler registration and
unregistration by providing ``drm_irq_install`` and
``drm_irq_uninstall`` functions. Those functions only support a single
interrupt per device, devices that use more than one IRQs need to be
handled manually.

Managed IRQ Registration
^^^^^^^^^^^^^^^^^^^^^^^^

``drm_irq_install`` starts by calling the irq_preinstall driver
operation. The operation is optional and must make sure that the
interrupt will not get fired by clearing all pending interrupt flags or
disabling the interrupt.

The passed-in IRQ will then be requested by a call to ``request_irq``.
If the DRIVER_IRQ_SHARED driver feature flag is set, a shared
(IRQF_SHARED) IRQ handler will be requested.

The IRQ handler function must be provided as the mandatory irq_handler
driver operation. It will get passed directly to ``request_irq`` and
thus has the same prototype as all IRQ handlers. It will get called with
a pointer to the DRM device as the second argument.

Finally the function calls the optional irq_postinstall driver
operation. The operation usually enables interrupts (excluding the
vblank interrupt, which is enabled separately), but drivers may choose
to enable/disable interrupts at a different time.

``drm_irq_uninstall`` is similarly used to uninstall an IRQ handler. It
starts by waking up all processes waiting on a vblank interrupt to make
sure they don't hang, and then calls the optional irq_uninstall driver
operation. The operation must disable all hardware interrupts. Finally
the function frees the IRQ by calling ``free_irq``.

Manual IRQ Registration
^^^^^^^^^^^^^^^^^^^^^^^

Drivers that require multiple interrupt handlers can't use the managed
IRQ registration functions. In that case IRQs must be registered and
unregistered manually (usually with the ``request_irq`` and ``free_irq``
functions, or their devm_* equivalent).

When manually registering IRQs, drivers must not set the
DRIVER_HAVE_IRQ driver feature flag, and must not provide the
irq_handler driver operation. They must set the ``drm_device``
``irq_enabled`` field to 1 upon registration of the IRQs, and clear it
to 0 after unregistering the IRQs.


Memory Manager Initialization
+++++++++++++++++++++++++++++

Every DRM driver requires a memory manager which must be initialized at
load time. DRM currently contains two memory managers, the Translation
Table Manager (TTM) and the Graphics Execution Manager (GEM). This
document describes the use of the GEM memory manager only. See
:ref:`drm-memory-management` for details.


Miscellaneous Device Configuration
++++++++++++++++++++++++++++++++++

Another task that may be necessary for PCI devices during configuration
is mapping the video BIOS. On many devices, the VBIOS describes device
configuration, LCD panel timings (if any), and contains flags indicating
device state. Mapping the BIOS can be done using the pci_map_rom()
call, a convenience function that takes care of mapping the actual ROM,
whether it has been shadowed into memory (typically at address 0xc0000)
or exists on the PCI device in the ROM BAR. Note that after the ROM has
been mapped and any necessary information has been extracted, it should
be unmapped; on many devices, the ROM address decoder is shared with
other BARs, so leaving it mapped could cause undesired behaviour like
hangs or memory corruption.


Bus-specific Device Registration and PCI Support
------------------------------------------------

A number of functions are provided to help with device registration. The
functions deal with PCI and platform devices respectively and are only
provided for historical reasons. These are all deprecated and shouldn't
be used in new drivers. Besides that there's a few helpers for pci
drivers.


.. toctree::
    :maxdepth: 1

    API-drm-pci-alloc
    API-drm-pci-free
    API-drm-get-pci-dev
    API-drm-pci-init
    API-drm-pci-exit
    API-drm-platform-init


.. _drm-memory-management:

Memory management
=================

Modern Linux systems require large amount of graphics memory to store
frame buffers, textures, vertices and other graphics-related data. Given
the very dynamic nature of many of that data, managing graphics memory
efficiently is thus crucial for the graphics stack and plays a central
role in the DRM infrastructure.

The DRM core includes two memory managers, namely Translation Table Maps
(TTM) and Graphics Execution Manager (GEM). TTM was the first DRM memory
manager to be developed and tried to be a one-size-fits-them all
solution. It provides a single userspace API to accommodate the need of
all hardware, supporting both Unified Memory Architecture (UMA) devices
and devices with dedicated video RAM (i.e. most discrete video cards).
This resulted in a large, complex piece of code that turned out to be
hard to use for driver development.

GEM started as an Intel-sponsored project in reaction to TTM's
complexity. Its design philosophy is completely different: instead of
providing a solution to every graphics memory-related problems, GEM
identified common code between drivers and created a support library to
share it. GEM has simpler initialization and execution requirements than
TTM, but has no video RAM management capabilities and is thus limited to
UMA devices.


The Translation Table Manager (TTM)
-----------------------------------

TTM design background and information belongs here.


TTM initialization
++++++++++++++++++

    **Warning**

    This section is outdated.

Drivers wishing to support TTM must fill out a drm_bo_driver
structure. The structure contains several fields with function pointers
for initializing the TTM, allocating and freeing memory, waiting for
command completion and fence synchronization, and memory migration. See
the radeon_ttm.c file for an example of usage.

The ttm_global_reference structure is made up of several fields:


.. code-block:: c

              struct ttm_global_reference {
                      enum ttm_global_types global_type;
                      size_t size;
                      void *object;
                      int (*init) (struct ttm_global_reference *);
                      void (*release) (struct ttm_global_reference *);
              };

There should be one global reference structure for your memory manager
as a whole, and there will be others for each object created by the
memory manager at runtime. Your global TTM should have a type of
TTM_GLOBAL_TTM_MEM. The size field for the global object should be
sizeof(struct ttm_mem_global), and the init and release hooks should
point at your driver-specific init and release routines, which probably
eventually call ttm_mem_global_init and ttm_mem_global_release,
respectively.

Once your global TTM accounting structure is set up and initialized by
calling ttm_global_item_ref() on it, you need to create a buffer
object TTM to provide a pool for buffer object allocation by clients and
the kernel itself. The type of this object should be
TTM_GLOBAL_TTM_BO, and its size should be sizeof(struct
ttm_bo_global). Again, driver-specific init and release functions may
be provided, likely eventually calling ttm_bo_global_init() and
ttm_bo_global_release(), respectively. Also, like the previous
object, ttm_global_item_ref() is used to create an initial reference
count for the TTM, which will call your initialization function.


.. _drm-gem:

The Graphics Execution Manager (GEM)
------------------------------------

The GEM design approach has resulted in a memory manager that doesn't
provide full coverage of all (or even all common) use cases in its
userspace or kernel API. GEM exposes a set of standard memory-related
operations to userspace and a set of helper functions to drivers, and
let drivers implement hardware-specific operations with their own
private API.

The GEM userspace API is described in the
`GEM - the Graphics Execution Manager <http://lwn.net/Articles/283798/>`__
article on LWN. While slightly outdated, the document provides a good
overview of the GEM API principles. Buffer allocation and read and write
operations, described as part of the common GEM API, are currently
implemented using driver-specific ioctls.

GEM is data-agnostic. It manages abstract buffer objects without knowing
what individual buffers contain. APIs that require knowledge of buffer
contents or purpose, such as buffer allocation or synchronization
primitives, are thus outside of the scope of GEM and must be implemented
using driver-specific ioctls.

On a fundamental level, GEM involves several operations:

-  Memory allocation and freeing
-  Command execution
-  Aperture management at command execution time

Buffer object allocation is relatively straightforward and largely
provided by Linux's shmem layer, which provides memory to back each
object.

Device-specific operations, such as command execution, pinning, buffer
read & write, mapping, and domain ownership transfers are left to
driver-specific ioctls.


GEM Initialization
++++++++++++++++++

Drivers that use GEM must set the DRIVER_GEM bit in the struct
``drm_driver`` ``driver_features`` field. The DRM core will then
automatically initialize the GEM core before calling the load operation.
Behind the scene, this will create a DRM Memory Manager object which
provides an address space pool for object allocation.

In a KMS configuration, drivers need to allocate and initialize a
command ring buffer following core GEM initialization if required by the
hardware. UMA devices usually have what is called a "stolen" memory
region, which provides space for the initial framebuffer and large,
contiguous memory regions required by the device. This space is
typically not managed by GEM, and must be initialized separately into
its own DRM MM object.


GEM Objects Creation
++++++++++++++++++++

GEM splits creation of GEM objects and allocation of the memory that
backs them in two distinct operations.

GEM objects are represented by an instance of struct ``drm_gem_object``.
Drivers usually need to extend GEM objects with private information and
thus create a driver-specific GEM object structure type that embeds an
instance of struct ``drm_gem_object``.

To create a GEM object, a driver allocates memory for an instance of its
specific GEM object type and initializes the embedded struct
``drm_gem_object`` with a call to ``drm_gem_object_init``. The function
takes a pointer to the DRM device, a pointer to the GEM object and the
buffer object size in bytes.

GEM uses shmem to allocate anonymous pageable memory.
``drm_gem_object_init`` will create an shmfs file of the requested size
and store it into the struct ``drm_gem_object`` ``filp`` field. The
memory is used as either main storage for the object when the graphics
hardware uses system memory directly or as a backing store otherwise.

Drivers are responsible for the actual physical pages allocation by
calling ``shmem_read_mapping_page_gfp`` for each page. Note that they
can decide to allocate pages when initializing the GEM object, or to
delay allocation until the memory is needed (for instance when a page
fault occurs as a result of a userspace memory access or when the driver
needs to start a DMA transfer involving the memory).

Anonymous pageable memory allocation is not always desired, for instance
when the hardware requires physically contiguous system memory as is
often the case in embedded devices. Drivers can create GEM objects with
no shmfs backing (called private GEM objects) by initializing them with
a call to ``drm_gem_private_object_init`` instead of
``drm_gem_object_init``. Storage for private GEM objects must be managed
by drivers.


GEM Objects Lifetime
++++++++++++++++++++

All GEM objects are reference-counted by the GEM core. References can be
acquired and release by ``calling drm_gem_object_reference`` and
``drm_gem_object_unreference`` respectively. The caller must hold the
``drm_device`` ``struct_mutex`` lock when calling
``drm_gem_object_reference``. As a convenience, GEM provides
``drm_gem_object_unreference_unlocked`` functions that can be called
without holding the lock.

When the last reference to a GEM object is released the GEM core calls
the ``drm_driver`` gem_free_object operation. That operation is
mandatory for GEM-enabled drivers and must free the GEM object and all
associated resources.


.. code-block:: c

    void (*gem_free_object) (struct drm_gem_object *obj);

Drivers are responsible for freeing all GEM object resources. This
includes the resources created by the GEM core, which need to be
released with ``drm_gem_object_release``.


GEM Objects Naming
++++++++++++++++++

Communication between userspace and the kernel refers to GEM objects
using local handles, global names or, more recently, file descriptors.
All of those are 32-bit integer values; the usual Linux kernel limits
apply to the file descriptors.

GEM handles are local to a DRM file. Applications get a handle to a GEM
object through a driver-specific ioctl, and can use that handle to refer
to the GEM object in other standard or driver-specific ioctls. Closing a
DRM file handle frees all its GEM handles and dereferences the
associated GEM objects.

To create a handle for a GEM object drivers call
``drm_gem_handle_create``. The function takes a pointer to the DRM file
and the GEM object and returns a locally unique handle. When the handle
is no longer needed drivers delete it with a call to
``drm_gem_handle_delete``. Finally the GEM object associated with a
handle can be retrieved by a call to ``drm_gem_object_lookup``.

Handles don't take ownership of GEM objects, they only take a reference
to the object that will be dropped when the handle is destroyed. To
avoid leaking GEM objects, drivers must make sure they drop the
reference(s) they own (such as the initial reference taken at object
creation time) as appropriate, without any special consideration for the
handle. For example, in the particular case of combined GEM object and
handle creation in the implementation of the dumb_create operation,
drivers must drop the initial reference to the GEM object before
returning the handle.

GEM names are similar in purpose to handles but are not local to DRM
files. They can be passed between processes to reference a GEM object
globally. Names can't be used directly to refer to objects in the DRM
API, applications must convert handles to names and names to handles
using the DRM_IOCTL_GEM_FLINK and DRM_IOCTL_GEM_OPEN ioctls
respectively. The conversion is handled by the DRM core without any
driver-specific support.

GEM also supports buffer sharing with dma-buf file descriptors through
PRIME. GEM-based drivers must use the provided helpers functions to
implement the exporting and importing correctly. See
:ref:`drm-prime-support`. Since sharing file descriptors is inherently
more secure than the easily guessable and global GEM names it is the
preferred buffer sharing mechanism. Sharing buffers through GEM names is
only supported for legacy userspace. Furthermore PRIME also allows
cross-device buffer sharing since it is based on dma-bufs.


.. _drm-gem-objects-mapping:

GEM Objects Mapping
+++++++++++++++++++

Because mapping operations are fairly heavyweight GEM favours
read/write-like access to buffers, implemented through driver-specific
ioctls, over mapping buffers to userspace. However, when random access
to the buffer is needed (to perform software rendering for instance),
direct access to the object can be more efficient.

The mmap system call can't be used directly to map GEM objects, as they
don't have their own file handle. Two alternative methods currently
co-exist to map GEM objects to userspace. The first method uses a
driver-specific ioctl to perform the mapping operation, calling
``do_mmap`` under the hood. This is often considered dubious, seems to
be discouraged for new GEM-enabled drivers, and will thus not be
described here.

The second method uses the mmap system call on the DRM file handle.


.. code-block:: c

    void *mmap(void *addr, size_t length, int prot, int flags, int fd,
                 off_t offset);

DRM identifies the GEM object to be mapped by a fake offset passed
through the mmap offset argument. Prior to being mapped, a GEM object
must thus be associated with a fake offset. To do so, drivers must call
``drm_gem_create_mmap_offset`` on the object.

Once allocated, the fake offset value must be passed to the application
in a driver-specific way and can then be used as the mmap offset
argument.

The GEM core provides a helper method ``drm_gem_mmap`` to handle object
mapping. The method can be set directly as the mmap file operation
handler. It will look up the GEM object based on the offset value and
set the VMA operations to the ``drm_driver`` ``gem_vm_ops`` field. Note
that ``drm_gem_mmap`` doesn't map memory to userspace, but relies on the
driver-provided fault handler to map pages individually.

To use ``drm_gem_mmap``, drivers must fill the struct ``drm_driver``
``gem_vm_ops`` field with a pointer to VM operations.


.. code-block:: c

    struct vm_operations_struct *gem_vm_ops

      struct vm_operations_struct {
              void (*open)(struct vm_area_struct * area);
              void (*close)(struct vm_area_struct * area);
              int (*fault)(struct vm_area_struct *vma, struct vm_fault *vmf);
      };

The open and close operations must update the GEM object reference
count. Drivers can use the ``drm_gem_vm_open`` and ``drm_gem_vm_close``
helper functions directly as open and close handlers.

The fault operation handler is responsible for mapping individual pages
to userspace when a page fault occurs. Depending on the memory
allocation scheme, drivers can allocate pages at fault time, or can
decide to allocate memory for the GEM object at the time the object is
created.

Drivers that want to map the GEM object upfront instead of handling page
faults can implement their own mmap file operation handler.


Memory Coherency
++++++++++++++++

When mapped to the device or used in a command buffer, backing pages for
an object are flushed to memory and marked write combined so as to be
coherent with the GPU. Likewise, if the CPU accesses an object after the
GPU has finished rendering to the object, then the object must be made
coherent with the CPU's view of memory, usually involving GPU cache
flushing of various kinds. This core CPU<->GPU coherency management is
provided by a device-specific ioctl, which evaluates an object's current
domain and performs any necessary flushing or synchronization to put the
object into the desired coherency domain (note that the object may be
busy, i.e. an active render target; in that case, setting the domain
blocks the client and waits for rendering to complete before performing
any necessary flushing operations).


Command Execution
+++++++++++++++++

Perhaps the most important GEM function for GPU devices is providing a
command execution interface to clients. Client programs construct
command buffers containing references to previously allocated memory
objects, and then submit them to GEM. At that point, GEM takes care to
bind all the objects into the GTT, execute the buffer, and provide
necessary synchronization between clients accessing the same buffers.
This often involves evicting some objects from the GTT and re-binding
others (a fairly expensive operation), and providing relocation support
which hides fixed GTT offsets from clients. Clients must take care not
to submit command buffers that reference more objects than can fit in
the GTT; otherwise, GEM will reject them and no rendering will occur.
Similarly, if several objects in the buffer require fence registers to
be allocated for correct rendering (e.g. 2D blits on pre-965 chips),
care must be taken not to require more fence registers than are
available to the client. Such resource management should be abstracted
from the client in libdrm.


GEM Function Reference
----------------------


.. toctree::
    :maxdepth: 1

    API-drm-gem-object-init
    API-drm-gem-private-object-init
    API-drm-gem-handle-delete
    API-drm-gem-dumb-destroy
    API-drm-gem-handle-create
    API-drm-gem-free-mmap-offset
    API-drm-gem-create-mmap-offset-size
    API-drm-gem-create-mmap-offset
    API-drm-gem-get-pages
    API-drm-gem-put-pages
    API-drm-gem-object-lookup
    API-drm-gem-object-free
    API-drm-gem-vm-open
    API-drm-gem-vm-close
    API-drm-gem-mmap-obj
    API-drm-gem-mmap
    API-struct-drm-gem-object
    API-drm-gem-object-reference
    API-drm-gem-object-unreference
    API-drm-gem-object-unreference-unlocked


VMA Offset Manager
------------------

The vma-manager is responsible to map arbitrary driver-dependent memory
regions into the linear user address-space. It provides offsets to the
caller which can then be used on the address_space of the drm-device.
It takes care to not overlap regions, size them appropriately and to not
confuse mm-core by inconsistent fake vm_pgoff fields. Drivers shouldn't
use this for object placement in VMEM. This manager should only be used
to manage mappings into linear user-space VMs.

We use drm_mm as backend to manage object allocations. But it is highly
optimized for alloc/free calls, not lookups. Hence, we use an rb-tree to
speed up offset lookups.

You must not use multiple offset managers on a single address_space.
Otherwise, mm-core will be unable to tear down memory mappings as the VM
will no longer be linear.

This offset manager works on page-based addresses. That is, every
argument and return code (with the exception of
``drm_vma_node_offset_addr``) is given in number of pages, not number of
bytes. That means, object sizes and offsets must always be page-aligned
(as usual). If you want to get a valid byte-based user-space address for
a given offset, please see ``drm_vma_node_offset_addr``.

Additionally to offset management, the vma offset manager also handles
access management. For every open-file context that is allowed to access
a given node, you must call ``drm_vma_node_allow``. Otherwise, an
``mmap`` call on this open-file with the offset of the node will fail
with -EACCES. To revoke access again, use ``drm_vma_node_revoke``.
However, the caller is responsible for destroying already existing
mappings, if required.


.. toctree::
    :maxdepth: 1

    API-drm-vma-offset-manager-init
    API-drm-vma-offset-manager-destroy
    API-drm-vma-offset-lookup-locked
    API-drm-vma-offset-add
    API-drm-vma-offset-remove
    API-drm-vma-node-allow
    API-drm-vma-node-revoke
    API-drm-vma-node-is-allowed
    API-drm-vma-offset-exact-lookup-locked
    API-drm-vma-offset-lock-lookup
    API-drm-vma-offset-unlock-lookup
    API-drm-vma-node-reset
    API-drm-vma-node-start
    API-drm-vma-node-size
    API-drm-vma-node-has-offset
    API-drm-vma-node-offset-addr
    API-drm-vma-node-unmap
    API-drm-vma-node-verify-access


.. _drm-prime-support:

PRIME Buffer Sharing
--------------------

PRIME is the cross device buffer sharing framework in drm, originally
created for the OPTIMUS range of multi-gpu platforms. To userspace PRIME
buffers are dma-buf based file descriptors.


Overview and Driver Interface
+++++++++++++++++++++++++++++

Similar to GEM global names, PRIME file descriptors are also used to
share buffer objects across processes. They offer additional security:
as file descriptors must be explicitly sent over UNIX domain sockets to
be shared between applications, they can't be guessed like the globally
unique GEM names.

Drivers that support the PRIME API must set the DRIVER_PRIME bit in the
struct ``drm_driver`` ``driver_features`` field, and implement the
prime_handle_to_fd and prime_fd_to_handle operations.


.. code-block:: c

    int (*prime_handle_to_fd)(struct drm_device *dev,
                              struct drm_file *file_priv, uint32_t handle,
                              uint32_t flags, int *prime_fd);
    int (*prime_fd_to_handle)(struct drm_device *dev,
                              struct drm_file *file_priv, int prime_fd,
                              uint32_t *handle);

Those two operations convert a handle to a PRIME file descriptor and
vice versa. Drivers must use the kernel dma-buf buffer sharing framework
to manage the PRIME file descriptors. Similar to the mode setting API
PRIME is agnostic to the underlying buffer object manager, as long as
handles are 32bit unsigned integers.

While non-GEM drivers must implement the operations themselves, GEM
drivers must use the ``drm_gem_prime_handle_to_fd`` and
``drm_gem_prime_fd_to_handle`` helper functions. Those helpers rely on
the driver gem_prime_export and gem_prime_import operations to
create a dma-buf instance from a GEM object (dma-buf exporter role) and
to create a GEM object from a dma-buf instance (dma-buf importer role).


.. code-block:: c

    struct dma_buf * (*gem_prime_export)(struct drm_device *dev,
                                 struct drm_gem_object *obj,
                                 int flags);
    struct drm_gem_object * (*gem_prime_import)(struct drm_device *dev,
                                                struct dma_buf *dma_buf);

These two operations are mandatory for GEM drivers that support PRIME.


PRIME Helper Functions
++++++++++++++++++++++

Drivers can implement ``gem_prime_export`` and ``gem_prime_import`` in
terms of simpler APIs by using the helper functions
``drm_gem_prime_export`` and ``drm_gem_prime_import``. These functions
implement dma-buf support in terms of six lower-level driver callbacks:

Export callbacks:

* ``gem_prime_pin`` (optional): prepare a GEM object for exporting *
``gem_prime_get_sg_table``: provide a scatter/gather table of pinned
pages * ``gem_prime_vmap``: vmap a buffer exported by your driver *
``gem_prime_vunmap``: vunmap a buffer exported by your driver *
``gem_prime_mmap`` (optional): mmap a buffer exported by your driver

Import callback:

* ``gem_prime_import_sg_table`` (import): produce a GEM object from
another driver's scatter/gather table


PRIME Function References
-------------------------


.. toctree::
    :maxdepth: 1

    API-drm-gem-dmabuf-release
    API-drm-gem-prime-export
    API-drm-gem-prime-handle-to-fd
    API-drm-gem-prime-import
    API-drm-gem-prime-fd-to-handle
    API-drm-prime-pages-to-sg
    API-drm-prime-sg-to-page-addr-arrays
    API-drm-prime-gem-destroy


DRM MM Range Allocator
----------------------


Overview
++++++++

drm_mm provides a simple range allocator. The drivers are free to use
the resource allocator from the linux core if it suits them, the upside
of drm_mm is that it's in the DRM core. Which means that it's easier to
extend for some of the crazier special purpose needs of gpus.

The main data struct is ``drm_mm``, allocations are tracked in
``drm_mm_node``. Drivers are free to embed either of them into their own
suitable datastructures. drm_mm itself will not do any allocations of
its own, so if drivers choose not to embed nodes they need to still
allocate them themselves.

The range allocator also supports reservation of preallocated blocks.
This is useful for taking over initial mode setting configurations from
the firmware, where an object needs to be created which exactly matches
the firmware's scanout target. As long as the range is still free it can
be inserted anytime after the allocator is initialized, which helps with
avoiding looped depencies in the driver load sequence.

drm_mm maintains a stack of most recently freed holes, which of all
simplistic datastructures seems to be a fairly decent approach to
clustering allocations and avoiding too much fragmentation. This means
free space searches are O(num_holes). Given that all the fancy features
drm_mm supports something better would be fairly complex and since gfx
thrashing is a fairly steep cliff not a real concern. Removing a node
again is O(1).

drm_mm supports a few features: Alignment and range restrictions can be
supplied. Further more every ``drm_mm_node`` has a color value (which is
just an opaqua unsigned long) which in conjunction with a driver
callback can be used to implement sophisticated placement restrictions.
The i915 DRM driver uses this to implement guard pages between
incompatible caching domains in the graphics TT.

Two behaviors are supported for searching and allocating: bottom-up and
top-down. The default is bottom-up. Top-down allocation can be used if
the memory area has different restrictions, or just to reduce
fragmentation.

Finally iteration helpers to walk all nodes and all holes are provided
as are some basic allocator dumpers for debugging.


LRU Scan/Eviction Support
+++++++++++++++++++++++++

Very often GPUs need to have continuous allocations for a given object.
When evicting objects to make space for a new one it is therefore not
most efficient when we simply start to select all objects from the tail
of an LRU until there's a suitable hole: Especially for big objects or
nodes that otherwise have special allocation constraints there's a good
chance we evict lots of (smaller) objects unecessarily.

The DRM range allocator supports this use-case through the scanning
interfaces. First a scan operation needs to be initialized with
``drm_mm_init_scan`` or ``drm_mm_init_scan_with_range``. The the driver
adds objects to the roaster (probably by walking an LRU list, but this
can be freely implemented) until a suitable hole is found or there's no
further evitable object.

The the driver must walk through all objects again in exactly the
reverse order to restore the allocator state. Note that while the
allocator is used in the scan mode no other operation is allowed.

Finally the driver evicts all objects selected in the scan. Adding and
removing an object is O(1), and since freeing a node is also O(1) the
overall complexity is O(scanned_objects). So like the free stack which
needs to be walked before a scan operation even begins this is linear in
the number of objects. It doesn't seem to hurt badly.


DRM MM Range Allocator Function References
------------------------------------------


.. toctree::
    :maxdepth: 1

    API-drm-mm-reserve-node
    API-drm-mm-insert-node-generic
    API-drm-mm-insert-node-in-range-generic
    API-drm-mm-remove-node
    API-drm-mm-replace-node
    API-drm-mm-init-scan
    API-drm-mm-init-scan-with-range
    API-drm-mm-scan-add-block
    API-drm-mm-scan-remove-block
    API-drm-mm-clean
    API-drm-mm-init
    API-drm-mm-takedown
    API-drm-mm-debug-table
    API-drm-mm-dump-table
    API-drm-mm-node-allocated
    API-drm-mm-initialized
    API-drm-mm-hole-node-start
    API-drm-mm-hole-node-end
    API-drm-mm-for-each-node
    API-drm-mm-for-each-hole
    API-drm-mm-insert-node
    API-drm-mm-insert-node-in-range


CMA Helper Functions Reference
------------------------------

The Contiguous Memory Allocator reserves a pool of memory at early boot
that is used to service requests for large blocks of contiguous memory.

The DRM GEM/CMA helpers use this allocator as a means to provide buffer
objects that are physically contiguous in memory. This is useful for
display drivers that are unable to map scattered buffers via an IOMMU.


.. toctree::
    :maxdepth: 1

    API-drm-gem-cma-create
    API-drm-gem-cma-free-object
    API-drm-gem-cma-dumb-create-internal
    API-drm-gem-cma-dumb-create
    API-drm-gem-cma-dumb-map-offset
    API-drm-gem-cma-mmap
    API-drm-gem-cma-describe
    API-drm-gem-cma-prime-get-sg-table
    API-drm-gem-cma-prime-import-sg-table
    API-drm-gem-cma-prime-mmap
    API-drm-gem-cma-prime-vmap
    API-drm-gem-cma-prime-vunmap
    API-struct-drm-gem-cma-object


.. _drm-mode-setting:

Mode Setting
============

Drivers must initialize the mode setting core by calling
``drm_mode_config_init`` on the DRM device. The function initializes the
``drm_device`` ``mode_config`` field and never fails. Once done, mode
configuration must be setup by initializing the following fields.

-  
   .. code-block:: c

       int min_width, min_height;
       int max_width, max_height;

   Minimum and maximum width and height of the frame buffers in pixel
   units.

-  
   .. code-block:: c

       struct drm_mode_config_funcs *funcs;

   Mode setting functions.


Display Modes Function Reference
--------------------------------


.. toctree::
    :maxdepth: 1

    API-enum-drm-mode-status
    API-struct-drm-display-mode
    API-drm-mode-is-stereo
    API-drm-mode-debug-printmodeline
    API-drm-mode-create
    API-drm-mode-destroy
    API-drm-mode-probed-add
    API-drm-cvt-mode
    API-drm-gtf-mode-complex
    API-drm-gtf-mode
    API-drm-display-mode-from-videomode
    API-drm-display-mode-to-videomode
    API-of-get-drm-display-mode
    API-drm-mode-set-name
    API-drm-mode-hsync
    API-drm-mode-vrefresh
    API-drm-mode-set-crtcinfo
    API-drm-mode-copy
    API-drm-mode-duplicate
    API-drm-mode-equal
    API-drm-mode-equal-no-clocks
    API-drm-mode-equal-no-clocks-no-stereo
    API-drm-mode-validate-basic
    API-drm-mode-validate-size
    API-drm-mode-prune-invalid
    API-drm-mode-sort
    API-drm-mode-connector-list-update
    API-drm-mode-parse-command-line-for-connector
    API-drm-mode-create-from-cmdline-mode


Atomic Mode Setting Function Reference
--------------------------------------


.. toctree::
    :maxdepth: 1

    API-drm-atomic-state-default-release
    API-drm-atomic-state-init
    API-drm-atomic-state-alloc
    API-drm-atomic-state-default-clear
    API-drm-atomic-state-clear
    API-drm-atomic-state-free
    API-drm-atomic-get-crtc-state
    API-drm-atomic-set-mode-for-crtc
    API-drm-atomic-set-mode-prop-for-crtc
    API-drm-atomic-crtc-set-property
    API-drm-atomic-get-plane-state
    API-drm-atomic-plane-set-property
    API-drm-atomic-get-connector-state
    API-drm-atomic-connector-set-property
    API-drm-atomic-set-crtc-for-plane
    API-drm-atomic-set-fb-for-plane
    API-drm-atomic-set-crtc-for-connector
    API-drm-atomic-add-affected-connectors
    API-drm-atomic-add-affected-planes
    API-drm-atomic-legacy-backoff
    API-drm-atomic-check-only
    API-drm-atomic-commit
    API-drm-atomic-async-commit
    API-drm-atomic-clean-old-fb
    API-drm-atomic-replace-property-blob
    API-drm-atomic-crtc-get-property
    API-drm-atomic-crtc-check
    API-drm-atomic-plane-get-property
    API-drm-atomic-plane-check
    API-drm-atomic-connector-get-property


Frame Buffer Abstraction
------------------------

Frame buffers are abstract memory objects that provide a source of
pixels to scanout to a CRTC. Applications explicitly request the
creation of frame buffers through the DRM_IOCTL_MODE_ADDFB(2) ioctls
and receive an opaque handle that can be passed to the KMS CRTC control,
plane configuration and page flip functions.

Frame buffers rely on the underneath memory manager for low-level memory
operations. When creating a frame buffer applications pass a memory
handle (or a list of memory handles for multi-planar formats) through
the ``drm_mode_fb_cmd2`` argument. For drivers using GEM as their
userspace buffer management interface this would be a GEM handle.
Drivers are however free to use their own backing storage object
handles, e.g. vmwgfx directly exposes special TTM handles to userspace
and so expects TTM handles in the create ioctl and not GEM handles.

The lifetime of a drm framebuffer is controlled with a reference count,
drivers can grab additional references with
``drm_framebuffer_reference``\ and drop them again with
``drm_framebuffer_unreference``. For driver-private framebuffers for
which the last reference is never dropped (e.g. for the fbdev
framebuffer when the struct ``drm_framebuffer`` is embedded into the
fbdev helper struct) drivers can manually clean up a framebuffer at
module unload time with ``drm_framebuffer_unregister_private``.


Dumb Buffer Objects
-------------------

The KMS API doesn't standardize backing storage object creation and
leaves it to driver-specific ioctls. Furthermore actually creating a
buffer object even for GEM-based drivers is done through a
driver-specific ioctl - GEM only has a common userspace interface for
sharing and destroying objects. While not an issue for full-fledged
graphics stacks that include device-specific userspace components (in
libdrm for instance), this limit makes DRM-based early boot graphics
unnecessarily complex.

Dumb objects partly alleviate the problem by providing a standard API to
create dumb buffers suitable for scanout, which can then be used to
create KMS frame buffers.

To support dumb objects drivers must implement the dumb_create,
dumb_destroy and dumb_map_offset operations.

-  
   .. code-block:: c

       int (*dumb_create)(struct drm_file *file_priv, struct drm_device *dev,
                          struct drm_mode_create_dumb *args);

   The dumb_create operation creates a driver object (GEM or TTM
   handle) suitable for scanout based on the width, height and depth
   from the struct ``drm_mode_create_dumb`` argument. It fills the
   argument's ``handle``, ``pitch`` and ``size`` fields with a handle
   for the newly created object and its line pitch and size in bytes.

-  
   .. code-block:: c

       int (*dumb_destroy)(struct drm_file *file_priv, struct drm_device *dev,
                           uint32_t handle);

   The dumb_destroy operation destroys a dumb object created by
   dumb_create.

-  
   .. code-block:: c

       int (*dumb_map_offset)(struct drm_file *file_priv, struct drm_device *dev,
                              uint32_t handle, uint64_t *offset);

   The dumb_map_offset operation associates an mmap fake offset with
   the object given by the handle and returns it. Drivers must use the
   ``drm_gem_create_mmap_offset`` function to associate the fake offset
   as described in :ref:`drm-gem-objects-mapping`.

Note that dumb objects may not be used for gpu acceleration, as has been
attempted on some ARM embedded platforms. Such drivers really must have
a hardware-specific ioctl to allocate suitable buffer objects.


Output Polling
--------------


.. code-block:: c

    void (*output_poll_changed)(struct drm_device *dev);

This operation notifies the driver that the status of one or more
connectors has changed. Drivers that use the fb helper can just call the
``drm_fb_helper_hotplug_event`` function to handle this operation.


Locking
-------

Beside some lookup structures with their own locking (which is hidden
behind the interface functions) most of the modeset state is protected
by the ``dev-<mode_config.lock`` mutex and additionally per-crtc locks
to allow cursor updates, pageflips and similar operations to occur
concurrently with background tasks like output detection. Operations
which cross domains like a full modeset always grab all locks. Drivers
there need to protect resources shared between crtcs with additional
locking. They also need to be careful to always grab the relevant crtc
locks if a modset functions touches crtc state, e.g. for load detection
(which does only grab the ``mode_config.lock`` to allow concurrent
screen updates on live crtcs).


.. _drm-kms-init:

KMS Initialization and Cleanup
==============================

A KMS device is abstracted and exposed as a set of planes, CRTCs,
encoders and connectors. KMS drivers must thus create and initialize all
those objects at load time after initializing mode setting.


CRTCs (struct drm_crtc)
-----------------------

A CRTC is an abstraction representing a part of the chip that contains a
pointer to a scanout buffer. Therefore, the number of CRTCs available
determines how many independent scanout buffers can be active at any
given time. The CRTC structure contains several fields to support this:
a pointer to some video memory (abstracted as a frame buffer object), a
display mode, and an (x, y) offset into the video memory to support
panning or configurations where one piece of video memory spans multiple
CRTCs.


CRTC Initialization
+++++++++++++++++++

A KMS device must create and register at least one struct ``drm_crtc``
instance. The instance is allocated and zeroed by the driver, possibly
as part of a larger structure, and registered with a call to
``drm_crtc_init`` with a pointer to CRTC functions.


Planes (struct drm_plane)
-------------------------

A plane represents an image source that can be blended with or overlayed
on top of a CRTC during the scanout process. Planes are associated with
a frame buffer to crop a portion of the image memory (source) and
optionally scale it to a destination size. The result is then blended
with or overlayed on top of a CRTC.

The DRM core recognizes three types of planes:

-  DRM_PLANE_TYPE_PRIMARY represents a "main" plane for a CRTC.
   Primary planes are the planes operated upon by CRTC modesetting and
   flipping operations described in the page_flip hook in
   drm_crtc_funcs
   .
-  DRM_PLANE_TYPE_CURSOR represents a "cursor" plane for a CRTC.
   Cursor planes are the planes operated upon by the
   DRM_IOCTL_MODE_CURSOR and DRM_IOCTL_MODE_CURSOR2 ioctls.
-  DRM_PLANE_TYPE_OVERLAY represents all non-primary, non-cursor
   planes. Some drivers refer to these types of planes as "sprites"
   internally.

For compatibility with legacy userspace, only overlay planes are made
available to userspace by default. Userspace clients may set the
DRM_CLIENT_CAP_UNIVERSAL_PLANES client capability bit to indicate
that they wish to receive a universal plane list containing all plane
types.


Plane Initialization
++++++++++++++++++++

To create a plane, a KMS drivers allocates and zeroes an instances of
struct ``drm_plane`` (possibly as part of a larger structure) and
registers it with a call to ``drm_universal_plane_init``. The function
takes a bitmask of the CRTCs that can be associated with the plane, a
pointer to the plane functions, a list of format supported formats, and
the type of plane (primary, cursor, or overlay) being initialized.

Cursor and overlay planes are optional. All drivers should provide one
primary plane per CRTC (although this requirement may change in the
future); drivers that do not wish to provide special handling for
primary planes may make use of the helper functions described in
:ref:`drm-kms-planehelpers` to create and register a primary plane
with standard capabilities.


Encoders (struct drm_encoder)
-----------------------------

An encoder takes pixel data from a CRTC and converts it to a format
suitable for any attached connectors. On some devices, it may be
possible to have a CRTC send data to more than one encoder. In that
case, both encoders would receive data from the same scanout buffer,
resulting in a "cloned" display configuration across the connectors
attached to each encoder.


Encoder Initialization
++++++++++++++++++++++

As for CRTCs, a KMS driver must create, initialize and register at least
one struct ``drm_encoder`` instance. The instance is allocated and
zeroed by the driver, possibly as part of a larger structure.

Drivers must initialize the struct ``drm_encoder`` ``possible_crtcs``
and ``possible_clones`` fields before registering the encoder. Both
fields are bitmasks of respectively the CRTCs that the encoder can be
connected to, and sibling encoders candidate for cloning.

After being initialized, the encoder must be registered with a call to
``drm_encoder_init``. The function takes a pointer to the encoder
functions and an encoder type. Supported types are

-  DRM_MODE_ENCODER_DAC for VGA and analog on DVI-I/DVI-A
-  DRM_MODE_ENCODER_TMDS for DVI, HDMI and (embedded) DisplayPort
-  DRM_MODE_ENCODER_LVDS for display panels
-  DRM_MODE_ENCODER_TVDAC for TV output (Composite, S-Video,
   Component, SCART)
-  DRM_MODE_ENCODER_VIRTUAL for virtual machine displays

Encoders must be attached to a CRTC to be used. DRM drivers leave
encoders unattached at initialization time. Applications (or the fbdev
compatibility layer when implemented) are responsible for attaching the
encoders they want to use to a CRTC.


Connectors (struct drm_connector)
---------------------------------

A connector is the final destination for pixel data on a device, and
usually connects directly to an external display device like a monitor
or laptop panel. A connector can only be attached to one encoder at a
time. The connector is also the structure where information about the
attached display is kept, so it contains fields for display data, EDID
data, DPMS & connection status, and information about modes supported on
the attached displays.


Connector Initialization
++++++++++++++++++++++++

Finally a KMS driver must create, initialize, register and attach at
least one struct ``drm_connector`` instance. The instance is created as
other KMS objects and initialized by setting the following fields.

``interlace_allowed``
    Whether the connector can handle interlaced modes.

``doublescan_allowed``
    Whether the connector can handle doublescan.

``display_info``
    Display information is filled from EDID information when a display
    is detected. For non hot-pluggable displays such as flat panels in
    embedded systems, the driver should initialize the
    ``display_info``.\ ``width_mm`` and ``display_info``.\ ``height_mm``
    fields with the physical size of the display.

``polled``
    Connector polling mode, a combination of

    DRM_CONNECTOR_POLL_HPD
        The connector generates hotplug events and doesn't need to be
        periodically polled. The CONNECT and DISCONNECT flags must not
        be set together with the HPD flag.

    DRM_CONNECTOR_POLL_CONNECT
        Periodically poll the connector for connection.

    DRM_CONNECTOR_POLL_DISCONNECT
        Periodically poll the connector for disconnection.

    Set to 0 for connectors that don't support connection status
    discovery.

The connector is then registered with a call to ``drm_connector_init``
with a pointer to the connector functions and a connector type, and
exposed through sysfs with a call to ``drm_connector_register``.

Supported connector types are

-  DRM_MODE_CONNECTOR_VGA
-  DRM_MODE_CONNECTOR_DVII
-  DRM_MODE_CONNECTOR_DVID
-  DRM_MODE_CONNECTOR_DVIA
-  DRM_MODE_CONNECTOR_Composite
-  DRM_MODE_CONNECTOR_SVIDEO
-  DRM_MODE_CONNECTOR_LVDS
-  DRM_MODE_CONNECTOR_Component
-  DRM_MODE_CONNECTOR_9PinDIN
-  DRM_MODE_CONNECTOR_DisplayPort
-  DRM_MODE_CONNECTOR_HDMIA
-  DRM_MODE_CONNECTOR_HDMIB
-  DRM_MODE_CONNECTOR_TV
-  DRM_MODE_CONNECTOR_eDP
-  DRM_MODE_CONNECTOR_VIRTUAL

Connectors must be attached to an encoder to be used. For devices that
map connectors to encoders 1:1, the connector should be attached at
initialization time with a call to
``drm_mode_connector_attach_encoder``. The driver must also set the
``drm_connector`` ``encoder`` field to point to the attached encoder.

Finally, drivers must initialize the connectors state change detection
with a call to ``drm_kms_helper_poll_init``. If at least one connector
is pollable but can't generate hotplug interrupts (indicated by the
DRM_CONNECTOR_POLL_CONNECT and DRM_CONNECTOR_POLL_DISCONNECT
connector flags), a delayed work will automatically be queued to
periodically poll for changes. Connectors that can generate hotplug
interrupts must be marked with the DRM_CONNECTOR_POLL_HPD flag
instead, and their interrupt handler must call
``drm_helper_hpd_irq_event``. The function will queue a delayed work to
check the state of all connectors, but no periodic polling will be done.


Connector Operations
++++++++++++++++++++

    **Note**

    Unless otherwise state, all operations are mandatory.

DPMS
^^^^


.. code-block:: c

    void (*dpms)(struct drm_connector *connector, int mode);

The DPMS operation sets the power state of a connector. The mode
argument is one of

-  DRM_MODE_DPMS_ON

-  DRM_MODE_DPMS_STANDBY

-  DRM_MODE_DPMS_SUSPEND

-  DRM_MODE_DPMS_OFF

In all but DPMS_ON mode the encoder to which the connector is attached
should put the display in low-power mode by driving its signals
appropriately. If more than one connector is attached to the encoder
care should be taken not to change the power state of other displays as
a side effect. Low-power mode should be propagated to the encoders and
CRTCs when all related connectors are put in low-power mode.

Modes
^^^^^


.. code-block:: c

    int (*fill_modes)(struct drm_connector *connector, uint32_t max_width,
                          uint32_t max_height);

Fill the mode list with all supported modes for the connector. If the
``max_width`` and ``max_height`` arguments are non-zero, the
implementation must ignore all modes wider than ``max_width`` or higher
than ``max_height``.

The connector must also fill in this operation its ``display_info``
``width_mm`` and ``height_mm`` fields with the connected display
physical size in millimeters. The fields should be set to 0 if the value
isn't known or is not applicable (for instance for projector devices).

Connection Status
^^^^^^^^^^^^^^^^^

The connection status is updated through polling or hotplug events when
supported (see :ref:`drm-kms-connector-polled`). The status value is
reported to userspace through ioctls and must not be used inside the
driver, as it only gets initialized by a call to
``drm_mode_getconnector`` from userspace.


.. code-block:: c

    enum drm_connector_status (*detect)(struct drm_connector *connector,
                                            bool force);

Check to see if anything is attached to the connector. The ``force``
parameter is set to false whilst polling or to true when checking the
connector due to user request. ``force`` can be used by the driver to
avoid expensive, destructive operations during automated probing.

Return connector_status_connected if something is connected to the
connector, connector_status_disconnected if nothing is connected and
connector_status_unknown if the connection state isn't known.

Drivers should only return connector_status_connected if the
connection status has really been probed as connected. Connectors that
can't detect the connection status, or failed connection status probes,
should return connector_status_unknown.


Cleanup
-------

The DRM core manages its objects' lifetime. When an object is not needed
anymore the core calls its destroy function, which must clean up and
free every resource allocated for the object. Every ``drm_*_init`` call
must be matched with a corresponding ``drm_*_cleanup`` call to cleanup
CRTCs (``drm_crtc_cleanup``), planes (``drm_plane_cleanup``), encoders
(``drm_encoder_cleanup``) and connectors (``drm_connector_cleanup``).
Furthermore, connectors that have been added to sysfs must be removed by
a call to ``drm_connector_unregister`` before calling
``drm_connector_cleanup``.

Connectors state change detection must be cleanup up with a call to
``drm_kms_helper_poll_fini``.


Output discovery and initialization example
-------------------------------------------


.. code-block:: c

    void intel_crt_init(struct drm_device *dev)
    {
        struct drm_connector *connector;
        struct intel_output *intel_output;

        intel_output = kzalloc(sizeof(struct intel_output), GFP_KERNEL);
        if (!intel_output)
            return;

        connector = &intel_output->base;
        drm_connector_init(dev, &intel_output->base,
                   &intel_crt_connector_funcs, DRM_MODE_CONNECTOR_VGA);

        drm_encoder_init(dev, &intel_output->enc, &intel_crt_enc_funcs,
                 DRM_MODE_ENCODER_DAC);

        drm_mode_connector_attach_encoder(&intel_output->base,
                          &intel_output->enc);

        /* Set up the DDC bus. */
        intel_output->ddc_bus = intel_i2c_create(dev, GPIOA, "CRTDDC_A");
        if (!intel_output->ddc_bus) {
            dev_printk(KERN_ERR, &dev->pdev->dev, "DDC bus registration "
                   "failed.\\n");
            return;
        }

        intel_output->type = INTEL_OUTPUT_ANALOG;
        connector->interlace_allowed = 0;
        connector->doublescan_allowed = 0;

        drm_encoder_helper_add(&intel_output->enc, &intel_crt_helper_funcs);
        drm_connector_helper_add(connector, &intel_crt_connector_helper_funcs);

        drm_connector_register(connector);
    }

In the example above (taken from the i915 driver), a CRTC, connector and
encoder combination is created. A device-specific i2c bus is also
created for fetching EDID data and performing monitor detection. Once
the process is complete, the new connector is registered with sysfs to
make its properties available to applications.


KMS API Functions
-----------------


.. toctree::
    :maxdepth: 1

    API-drm-get-connector-status-name
    API-drm-get-subpixel-order-name
    API-drm-get-format-name
    API-drm-mode-object-find
    API-drm-framebuffer-init
    API-drm-framebuffer-lookup
    API-drm-framebuffer-unreference
    API-drm-framebuffer-reference
    API-drm-framebuffer-unregister-private
    API-drm-framebuffer-cleanup
    API-drm-framebuffer-remove
    API-drm-crtc-init-with-planes
    API-drm-crtc-cleanup
    API-drm-crtc-index
    API-drm-display-info-set-bus-formats
    API-drm-connector-init
    API-drm-connector-cleanup
    API-drm-connector-register
    API-drm-connector-unregister
    API-drm-connector-unplug-all
    API-drm-encoder-init
    API-drm-encoder-index
    API-drm-encoder-cleanup
    API-drm-universal-plane-init
    API-drm-plane-init
    API-drm-plane-cleanup
    API-drm-plane-index
    API-drm-plane-from-index
    API-drm-plane-force-disable
    API-drm-mode-create-dvi-i-properties
    API-drm-mode-create-tv-properties
    API-drm-mode-create-scaling-mode-property
    API-drm-mode-create-aspect-ratio-property
    API-drm-mode-create-dirty-info-property
    API-drm-mode-create-suggested-offset-properties
    API-drm-mode-set-config-internal
    API-drm-crtc-get-hv-timing
    API-drm-crtc-check-viewport
    API-drm-mode-legacy-fb-format
    API-drm-property-create
    API-drm-property-create-enum
    API-drm-property-create-bitmask
    API-drm-property-create-range
    API-drm-property-create-signed-range
    API-drm-property-create-object
    API-drm-property-create-bool
    API-drm-property-add-enum
    API-drm-property-destroy
    API-drm-object-attach-property
    API-drm-object-property-set-value
    API-drm-object-property-get-value
    API-drm-property-create-blob
    API-drm-property-unreference-blob
    API-drm-property-reference-blob
    API-drm-property-lookup-blob
    API-drm-mode-connector-set-path-property
    API-drm-mode-connector-set-tile-property
    API-drm-mode-connector-update-edid-property
    API-drm-mode-plane-set-obj-prop
    API-drm-mode-connector-attach-encoder
    API-drm-mode-crtc-set-gamma-size
    API-drm-mode-config-reset
    API-drm-fb-get-bpp-depth
    API-drm-format-num-planes
    API-drm-format-plane-cpp
    API-drm-format-horz-chroma-subsampling
    API-drm-format-vert-chroma-subsampling
    API-drm-format-plane-width
    API-drm-format-plane-height
    API-drm-rotation-simplify
    API-drm-mode-config-init
    API-drm-mode-config-cleanup
    API-drm-mode-get-tile-group
    API-drm-mode-create-tile-group


KMS Data Structures
-------------------


.. toctree::
    :maxdepth: 1

    API-struct-drm-framebuffer-funcs
    API-struct-drm-crtc-state
    API-struct-drm-crtc-funcs
    API-struct-drm-crtc
    API-struct-drm-connector-state
    API-struct-drm-connector-funcs
    API-struct-drm-encoder-funcs
    API-struct-drm-encoder
    API-struct-drm-connector
    API-struct-drm-plane-state
    API-struct-drm-plane-funcs
    API-struct-drm-plane
    API-struct-drm-bridge-funcs
    API-struct-drm-bridge
    API-struct-drm-atomic-state
    API-struct-drm-mode-set
    API-struct-drm-mode-config-funcs
    API-struct-drm-mode-config
    API-drm-for-each-plane-mask
    API-drm-for-each-encoder-mask
    API-drm-crtc-mask
    API-drm-encoder-crtc-ok


KMS Locking
-----------

As KMS moves toward more fine grained locking, and atomic ioctl where
userspace can indirectly control locking order, it becomes necessary to
use ww_mutex and acquire-contexts to avoid deadlocks. But because the
locking is more distributed around the driver code, we want a bit of
extra utility/tracking out of our acquire-ctx. This is provided by
drm_modeset_lock / drm_modeset_acquire_ctx.

For basic principles of ww_mutex, see:
Documentation/locking/ww-mutex-design.txt

The basic usage pattern is to:

drm_modeset_acquire_init( ``ctx``) retry: foreach (lock in
random_ordered_set_of_locks) { ret = drm_modeset_lock(lock,
``ctx``) if (ret == -EDEADLK) { drm_modeset_backoff( ``ctx``); goto
retry; } } ... do stuff ... drm_modeset_drop_locks( ``ctx``);
drm_modeset_acquire_fini( ``ctx``);


.. toctree::
    :maxdepth: 1

    API-struct-drm-modeset-acquire-ctx
    API-struct-drm-modeset-lock
    API-drm-modeset-lock-init
    API-drm-modeset-lock-fini
    API-drm-modeset-is-locked
    API-drm-modeset-lock-all
    API-drm-modeset-unlock-all
    API-drm-modeset-lock-crtc
    API-drm-modeset-legacy-acquire-ctx
    API-drm-modeset-unlock-crtc
    API-drm-warn-on-modeset-not-all-locked
    API-drm-modeset-acquire-init
    API-drm-modeset-acquire-fini
    API-drm-modeset-drop-locks
    API-drm-modeset-backoff
    API-drm-modeset-backoff-interruptible
    API-drm-modeset-lock
    API-drm-modeset-lock-interruptible
    API-drm-modeset-unlock
    API-drm-modeset-lock-all-ctx


Mode Setting Helper Functions
=============================

The plane, CRTC, encoder and connector functions provided by the drivers
implement the DRM API. They're called by the DRM core and ioctl handlers
to handle device state changes and configuration request. As
implementing those functions often requires logic not specific to
drivers, mid-layer helper functions are available to avoid duplicating
boilerplate code.

The DRM core contains one mid-layer implementation. The mid-layer
provides implementations of several plane, CRTC, encoder and connector
functions (called from the top of the mid-layer) that pre-process
requests and call lower-level functions provided by the driver (at the
bottom of the mid-layer). For instance, the
``drm_crtc_helper_set_config`` function can be used to fill the struct
``drm_crtc_funcs`` ``set_config`` field. When called, it will split the
set_config operation in smaller, simpler operations and call the driver
to handle them.

To use the mid-layer, drivers call ``drm_crtc_helper_add``,
``drm_encoder_helper_add`` and ``drm_connector_helper_add`` functions to
install their mid-layer bottom operations handlers, and fill the
``drm_crtc_funcs``, ``drm_encoder_funcs`` and ``drm_connector_funcs``
structures with pointers to the mid-layer top API functions. Installing
the mid-layer bottom operation handlers is best done right after
registering the corresponding KMS object.

The mid-layer is not split between CRTC, encoder and connector
operations. To use it, a driver must provide bottom functions for all of
the three KMS entities.


Atomic Modeset Helper Functions Reference
-----------------------------------------


Overview
++++++++

This helper library provides implementations of check and commit
functions on top of the CRTC modeset helper callbacks and the plane
helper callbacks. It also provides convenience implementations for the
atomic state handling callbacks for drivers which don't need to subclass
the drm core structures to add their own additional internal state.

This library also provides default implementations for the check
callback in ``drm_atomic_helper_check`` and for the commit callback with
``drm_atomic_helper_commit``. But the individual stages and callbacks
are exposed to allow drivers to mix and match and e.g. use the plane
helpers only together with a driver private modeset implementation.

This library also provides implementations for all the legacy driver
interfaces on top of the atomic interface. See
``drm_atomic_helper_set_config``, ``drm_atomic_helper_disable_plane``,
``drm_atomic_helper_disable_plane`` and the various functions to
implement set_property callbacks. New drivers must not implement these
functions themselves but must use the provided helpers.

The atomic helper uses the same function table structures as all other
modesetting helpers. See the documentation for struct
``drm_crtc_helper_funcs``, struct ``drm_encoder_helper_funcs`` and
struct ``drm_connector_helper_funcs``. It also shares the struct
``drm_plane_helper_funcs`` function table with the plane helpers.


Implementing Asynchronous Atomic Commit
+++++++++++++++++++++++++++++++++++++++

For now the atomic helpers don't support async commit directly. If there
is real need it could be added though, using the dma-buf fence
infrastructure for generic synchronization with outstanding rendering.

For now drivers have to implement async commit themselves, with the
following sequence being the recommended one:

1. Run ``drm_atomic_helper_prepare_planes`` first. This is the only
function which commit needs to call which can fail, so we want to run it
first and synchronously.

2. Synchronize with any outstanding asynchronous commit worker threads
which might be affected the new state update. This can be done by either
cancelling or flushing the work items, depending upon whether the driver
can deal with cancelled updates. Note that it is important to ensure
that the framebuffer cleanup is still done when cancelling.

For sufficient parallelism it is recommended to have a work item per
crtc (for updates which don't touch global state) and a global one. Then
we only need to synchronize with the crtc work items for changed crtcs
and the global work item, which allows nice concurrent updates on
disjoint sets of crtcs.

3. The software state is updated synchronously with
``drm_atomic_helper_swap_state``. Doing this under the protection of all
modeset locks means concurrent callers never see inconsistent state. And
doing this while it's guaranteed that no relevant async worker runs
means that async workers do not need grab any locks. Actually they must
not grab locks, for otherwise the work flushing will deadlock.

4. Schedule a work item to do all subsequent steps, using the split-out
commit helpers: a) pre-plane commit b) plane commit c) post-plane commit
and then cleaning up the framebuffers after the old framebuffer is no
longer being displayed.


Atomic State Reset and Initialization
+++++++++++++++++++++++++++++++++++++

Both the drm core and the atomic helpers assume that there is always the
full and correct atomic software state for all connectors, CRTCs and
planes available. Which is a bit a problem on driver load and also after
system suspend. One way to solve this is to have a hardware state
read-out infrastructure which reconstructs the full software state (e.g.
the i915 driver).

The simpler solution is to just reset the software state to everything
off, which is easiest to do by calling ``drm_mode_config_reset``. To
facilitate this the atomic helpers provide default reset implementations
for all hooks.

On the upside the precise state tracking of atomic simplifies system
suspend and resume a lot. For drivers using ``drm_mode_config_reset`` a
complete recipe is implemented in ``drm_atomic_helper_suspend`` and
``drm_atomic_helper_resume``. For other drivers the building blocks are
split out, see the documentation for these functions.


.. toctree::
    :maxdepth: 1

    API-drm-atomic-crtc-for-each-plane
    API-drm-atomic-crtc-state-for-each-plane
    API-drm-atomic-helper-check-modeset
    API-drm-atomic-helper-check-planes
    API-drm-atomic-helper-check
    API-drm-atomic-helper-update-legacy-modeset-state
    API-drm-atomic-helper-commit-modeset-disables
    API-drm-atomic-helper-commit-modeset-enables
    API-drm-atomic-helper-framebuffer-changed
    API-drm-atomic-helper-wait-for-vblanks
    API-drm-atomic-helper-commit
    API-drm-atomic-helper-prepare-planes
    API-drm-atomic-helper-commit-planes
    API-drm-atomic-helper-commit-planes-on-crtc
    API-drm-atomic-helper-disable-planes-on-crtc
    API-drm-atomic-helper-cleanup-planes
    API-drm-atomic-helper-swap-state
    API-drm-atomic-helper-update-plane
    API-drm-atomic-helper-disable-plane
    API-drm-atomic-helper-set-config
    API-drm-atomic-helper-disable-all
    API-drm-atomic-helper-suspend
    API-drm-atomic-helper-resume
    API-drm-atomic-helper-crtc-set-property
    API-drm-atomic-helper-plane-set-property
    API-drm-atomic-helper-connector-set-property
    API-drm-atomic-helper-page-flip
    API-drm-atomic-helper-connector-dpms
    API-drm-atomic-helper-crtc-reset
    API---drm-atomic-helper-crtc-duplicate-state
    API-drm-atomic-helper-crtc-duplicate-state
    API---drm-atomic-helper-crtc-destroy-state
    API-drm-atomic-helper-crtc-destroy-state
    API-drm-atomic-helper-plane-reset
    API---drm-atomic-helper-plane-duplicate-state
    API-drm-atomic-helper-plane-duplicate-state
    API---drm-atomic-helper-plane-destroy-state
    API-drm-atomic-helper-plane-destroy-state
    API---drm-atomic-helper-connector-reset
    API-drm-atomic-helper-connector-reset
    API---drm-atomic-helper-connector-duplicate-state
    API-drm-atomic-helper-connector-duplicate-state
    API-drm-atomic-helper-duplicate-state
    API---drm-atomic-helper-connector-destroy-state
    API-drm-atomic-helper-connector-destroy-state
    API-drm-atomic-helper-legacy-gamma-set


Modeset Helper Reference for Common Vtables
-------------------------------------------


.. toctree::
    :maxdepth: 1

    API-struct-drm-crtc-helper-funcs
    API-drm-crtc-helper-add
    API-struct-drm-encoder-helper-funcs
    API-drm-encoder-helper-add
    API-struct-drm-connector-helper-funcs
    API-drm-connector-helper-add
    API-struct-drm-plane-helper-funcs
    API-drm-plane-helper-add

The DRM mode setting helper functions are common code for drivers to use
if they wish. Drivers are not forced to use this code in their
implementations but it would be useful if the code they do use at least
provides a consistent interface and operation to userspace. Therefore it
is highly recommended to use the provided helpers as much as possible.

Because there is only one pointer per modeset object to hold a vfunc
table for helper libraries they are by necessity shared among the
different helpers.

To make this clear all the helper vtables are pulled together in this
location here.


Legacy CRTC/Modeset Helper Functions Reference
----------------------------------------------


.. toctree::
    :maxdepth: 1

    API-drm-helper-move-panel-connectors-to-head
    API-drm-helper-encoder-in-use
    API-drm-helper-crtc-in-use
    API-drm-helper-disable-unused-functions
    API-drm-crtc-helper-set-mode
    API-drm-crtc-helper-set-config
    API-drm-helper-connector-dpms
    API-drm-helper-mode-fill-fb-struct
    API-drm-helper-resume-force-mode
    API-drm-helper-crtc-mode-set
    API-drm-helper-crtc-mode-set-base
    API-drm-helper-crtc-enable-color-mgmt

The CRTC modeset helper library provides a default set_config
implementation in ``drm_crtc_helper_set_config``. Plus a few other
convenience functions using the same callbacks which drivers can use to
e.g. restore the modeset configuration on resume with
``drm_helper_resume_force_mode``.

Note that this helper library doesn't track the current power state of
CRTCs and encoders. It can call callbacks like ->``dpms`` even though
the hardware is already in the desired state. This deficiency has been
fixed in the atomic helpers.

The driver callbacks are mostly compatible with the atomic modeset
helpers, except for the handling of the primary plane: Atomic helpers
require that the primary plane is implemented as a real standalone plane
and not directly tied to the CRTC state. For easier transition this
library provides functions to implement the old semantics required by
the CRTC helpers using the new plane and atomic helper callbacks.

Drivers are strongly urged to convert to the atomic helpers (by way of
first converting to the plane helpers). New drivers must not use these
functions but need to implement the atomic interface instead,
potentially using the atomic helpers for that.

These legacy modeset helpers use the same function table structures as
all other modesetting helpers. See the documentation for struct
``drm_crtc_helper_funcs``, struct ``drm_encoder_helper_funcs`` and
struct ``drm_connector_helper_funcs``.


Output Probing Helper Functions Reference
-----------------------------------------

This library provides some helper code for output probing. It provides
an implementation of the core connector->fill_modes interface with
drm_helper_probe_single_connector_modes.

It also provides support for polling connectors with a work item and for
generic hotplug interrupt handling where the driver doesn't or cannot
keep track of a per-connector hpd interrupt.

This helper library can be used independently of the modeset helper
library. Drivers can also overwrite different parts e.g. use their own
hotplug handling code to avoid probing unrelated outputs.

The probe helpers share the function table structures with other display
helper libraries. See struct ``drm_connector_helper_funcs`` for the
details.


.. toctree::
    :maxdepth: 1

    API-drm-kms-helper-poll-enable-locked
    API-drm-helper-probe-single-connector-modes
    API-drm-kms-helper-hotplug-event
    API-drm-kms-helper-poll-disable
    API-drm-kms-helper-poll-enable
    API-drm-kms-helper-poll-init
    API-drm-kms-helper-poll-fini
    API-drm-helper-hpd-irq-event


fbdev Helper Functions Reference
--------------------------------

The fb helper functions are useful to provide an fbdev on top of a drm
kernel mode setting driver. They can be used mostly independently from
the crtc helper functions used by many drivers to implement the kernel
mode setting interfaces.

Initialization is done as a four-step process with
``drm_fb_helper_prepare``, ``drm_fb_helper_init``,
``drm_fb_helper_single_add_all_connectors`` and
``drm_fb_helper_initial_config``. Drivers with fancier requirements than
the default behaviour can override the third step with their own code.
Teardown is done with ``drm_fb_helper_fini``.

At runtime drivers should restore the fbdev console by calling
``drm_fb_helper_restore_fbdev_mode_unlocked`` from their ->lastclose
callback. They should also notify the fb helper code from updates to the
output configuration by calling ``drm_fb_helper_hotplug_event``. For
easier integration with the output polling code in drm_crtc_helper.c
the modeset code provides a ->output_poll_changed callback.

All other functions exported by the fb helper library can be used to
implement the fbdev driver interface by the driver.

It is possible, though perhaps somewhat tricky, to implement race-free
hotplug detection using the fbdev helpers. The ``drm_fb_helper_prepare``
helper must be called first to initialize the minimum required to make
hotplug detection work. Drivers also need to make sure to properly set
up the dev->mode_config.funcs member. After calling
``drm_kms_helper_poll_init`` it is safe to enable interrupts and start
processing hotplug events. At the same time, drivers should initialize
all modeset objects such as CRTCs, encoders and connectors. To finish up
the fbdev helper initialization, the ``drm_fb_helper_init`` function is
called. To probe for all attached displays and set up an initial
configuration using the detected hardware, drivers should call
``drm_fb_helper_single_add_all_connectors`` followed by
``drm_fb_helper_initial_config``.


.. toctree::
    :maxdepth: 1

    API-drm-fb-helper-single-add-all-connectors
    API-drm-fb-helper-debug-enter
    API-drm-fb-helper-debug-leave
    API-drm-fb-helper-restore-fbdev-mode-unlocked
    API-drm-fb-helper-blank
    API-drm-fb-helper-prepare
    API-drm-fb-helper-init
    API-drm-fb-helper-alloc-fbi
    API-drm-fb-helper-unregister-fbi
    API-drm-fb-helper-release-fbi
    API-drm-fb-helper-unlink-fbi
    API-drm-fb-helper-sys-read
    API-drm-fb-helper-sys-write
    API-drm-fb-helper-sys-fillrect
    API-drm-fb-helper-sys-copyarea
    API-drm-fb-helper-sys-imageblit
    API-drm-fb-helper-cfb-fillrect
    API-drm-fb-helper-cfb-copyarea
    API-drm-fb-helper-cfb-imageblit
    API-drm-fb-helper-set-suspend
    API-drm-fb-helper-setcmap
    API-drm-fb-helper-check-var
    API-drm-fb-helper-set-par
    API-drm-fb-helper-pan-display
    API-drm-fb-helper-fill-fix
    API-drm-fb-helper-fill-var
    API-drm-fb-helper-initial-config
    API-drm-fb-helper-hotplug-event
    API-struct-drm-fb-helper-surface-size
    API-struct-drm-fb-helper-funcs
    API-struct-drm-fb-helper


Display Port Helper Functions Reference
---------------------------------------

These functions contain some common logic and helpers at various
abstraction levels to deal with Display Port sink devices and related
things like DP aux channel transfers, EDID reading over DP aux channels,
decoding certain DPCD blocks, ...

The DisplayPort AUX channel is an abstraction to allow generic, driver-
independent access to AUX functionality. Drivers can take advantage of
this by filling in the fields of the drm_dp_aux structure.

Transactions are described using a hardware-independent
drm_dp_aux_msg structure, which is passed into a driver's
.\ ``transfer`` implementation. Both native and I2C-over-AUX
transactions are supported.


.. toctree::
    :maxdepth: 1

    API-struct-drm-dp-aux-msg
    API-struct-drm-dp-aux
    API-drm-dp-dpcd-readb
    API-drm-dp-dpcd-writeb
    API-drm-dp-dpcd-read
    API-drm-dp-dpcd-write
    API-drm-dp-dpcd-read-link-status
    API-drm-dp-link-probe
    API-drm-dp-link-power-up
    API-drm-dp-link-power-down
    API-drm-dp-link-configure
    API-drm-dp-aux-register
    API-drm-dp-aux-unregister


Display Port MST Helper Functions Reference
-------------------------------------------

These functions contain parts of the DisplayPort 1.2a MultiStream
Transport protocol. The helpers contain a topology manager and bandwidth
manager. The helpers encapsulate the sending and received of sideband
msgs.


.. toctree::
    :maxdepth: 1

    API-struct-drm-dp-vcpi
    API-struct-drm-dp-mst-port
    API-struct-drm-dp-mst-branch
    API-struct-drm-dp-mst-topology-mgr
    API-drm-dp-update-payload-part1
    API-drm-dp-update-payload-part2
    API-drm-dp-mst-topology-mgr-set-mst
    API-drm-dp-mst-topology-mgr-suspend
    API-drm-dp-mst-topology-mgr-resume
    API-drm-dp-mst-hpd-irq
    API-drm-dp-mst-detect-port
    API-drm-dp-mst-port-has-audio
    API-drm-dp-mst-get-edid
    API-drm-dp-find-vcpi-slots
    API-drm-dp-mst-allocate-vcpi
    API-drm-dp-mst-reset-vcpi-slots
    API-drm-dp-mst-deallocate-vcpi
    API-drm-dp-check-act-status
    API-drm-dp-calc-pbn-mode
    API-drm-dp-mst-dump-topology
    API-drm-dp-mst-topology-mgr-init
    API-drm-dp-mst-topology-mgr-destroy


MIPI DSI Helper Functions Reference
-----------------------------------

These functions contain some common logic and helpers to deal with MIPI
DSI peripherals.

Helpers are provided for a number of standard MIPI DSI command as well
as a subset of the MIPI DCS command set.


.. toctree::
    :maxdepth: 1

    API-struct-mipi-dsi-msg
    API-struct-mipi-dsi-packet
    API-struct-mipi-dsi-host-ops
    API-struct-mipi-dsi-host
    API-struct-mipi-dsi-device-info
    API-struct-mipi-dsi-device
    API-mipi-dsi-pixel-format-to-bpp
    API-enum-mipi-dsi-dcs-tear-mode
    API-struct-mipi-dsi-driver
    API-of-find-mipi-dsi-device-by-node
    API-mipi-dsi-device-register-full
    API-mipi-dsi-device-unregister
    API-of-find-mipi-dsi-host-by-node
    API-mipi-dsi-attach
    API-mipi-dsi-detach
    API-mipi-dsi-packet-format-is-short
    API-mipi-dsi-packet-format-is-long
    API-mipi-dsi-create-packet
    API-mipi-dsi-shutdown-peripheral
    API-mipi-dsi-turn-on-peripheral
    API-mipi-dsi-generic-write
    API-mipi-dsi-generic-read
    API-mipi-dsi-dcs-write-buffer
    API-mipi-dsi-dcs-write
    API-mipi-dsi-dcs-read
    API-mipi-dsi-dcs-nop
    API-mipi-dsi-dcs-soft-reset
    API-mipi-dsi-dcs-get-power-mode
    API-mipi-dsi-dcs-get-pixel-format
    API-mipi-dsi-dcs-enter-sleep-mode
    API-mipi-dsi-dcs-exit-sleep-mode
    API-mipi-dsi-dcs-set-display-off
    API-mipi-dsi-dcs-set-display-on
    API-mipi-dsi-dcs-set-column-address
    API-mipi-dsi-dcs-set-page-address
    API-mipi-dsi-dcs-set-tear-off
    API-mipi-dsi-dcs-set-tear-on
    API-mipi-dsi-dcs-set-pixel-format
    API-mipi-dsi-driver-register-full
    API-mipi-dsi-driver-unregister


EDID Helper Functions Reference
-------------------------------


.. toctree::
    :maxdepth: 1

    API-drm-edid-header-is-valid
    API-drm-edid-block-valid
    API-drm-edid-is-valid
    API-drm-do-get-edid
    API-drm-probe-ddc
    API-drm-get-edid
    API-drm-get-edid-switcheroo
    API-drm-edid-duplicate
    API-drm-match-cea-mode
    API-drm-get-cea-aspect-ratio
    API-drm-edid-to-eld
    API-drm-edid-to-sad
    API-drm-edid-to-speaker-allocation
    API-drm-av-sync-delay
    API-drm-select-eld
    API-drm-detect-hdmi-monitor
    API-drm-detect-monitor-audio
    API-drm-rgb-quant-range-selectable
    API-drm-add-edid-modes
    API-drm-add-modes-noedid
    API-drm-set-preferred-mode
    API-drm-hdmi-avi-infoframe-from-display-mode
    API-drm-hdmi-vendor-infoframe-from-display-mode


Rectangle Utilities Reference
-----------------------------

Utility functions to help manage rectangular areas for clipping,
scaling, etc. calculations.


.. toctree::
    :maxdepth: 1

    API-struct-drm-rect
    API-drm-rect-adjust-size
    API-drm-rect-translate
    API-drm-rect-downscale
    API-drm-rect-width
    API-drm-rect-height
    API-drm-rect-visible
    API-drm-rect-equals
    API-drm-rect-intersect
    API-drm-rect-clip-scaled
    API-drm-rect-calc-hscale
    API-drm-rect-calc-vscale
    API-drm-rect-calc-hscale-relaxed
    API-drm-rect-calc-vscale-relaxed
    API-drm-rect-debug-print
    API-drm-rect-rotate
    API-drm-rect-rotate-inv


Flip-work Helper Reference
--------------------------

Util to queue up work to run from work-queue context after flip/vblank.
Typically this can be used to defer unref of framebuffer's, cursor bo's,
etc until after vblank. The APIs are all thread-safe. Moreover,
drm_flip_work_queue_task and drm_flip_work_queue can be called in
atomic context.


.. toctree::
    :maxdepth: 1

    API-struct-drm-flip-task
    API-struct-drm-flip-work
    API-drm-flip-work-allocate-task
    API-drm-flip-work-queue-task
    API-drm-flip-work-queue
    API-drm-flip-work-commit
    API-drm-flip-work-init
    API-drm-flip-work-cleanup


HDMI Infoframes Helper Reference
--------------------------------

Strictly speaking this is not a DRM helper library but generally useable
by any driver interfacing with HDMI outputs like v4l or alsa drivers.
But it nicely fits into the overall topic of mode setting helper
libraries and hence is also included here.


.. toctree::
    :maxdepth: 1

    API-struct-hdmi-infoframe
    API-hdmi-avi-infoframe-init
    API-hdmi-avi-infoframe-pack
    API-hdmi-spd-infoframe-init
    API-hdmi-spd-infoframe-pack
    API-hdmi-audio-infoframe-init
    API-hdmi-audio-infoframe-pack
    API-hdmi-vendor-infoframe-init
    API-hdmi-vendor-infoframe-pack
    API-hdmi-infoframe-pack
    API-hdmi-infoframe-log
    API-hdmi-infoframe-unpack


Plane Helper Reference
----------------------


.. toctree::
    :maxdepth: 1

    API-drm-plane-helper-check-update
    API-drm-primary-helper-update
    API-drm-primary-helper-disable
    API-drm-primary-helper-destroy
    API-drm-crtc-init
    API-drm-plane-helper-update
    API-drm-plane-helper-disable

This helper library has two parts. The first part has support to
implement primary plane support on top of the normal CRTC configuration
interface. Since the legacy ->set_config interface ties the primary
plane together with the CRTC state this does not allow userspace to
disable the primary plane itself. To avoid too much duplicated code use
``drm_plane_helper_check_update`` which can be used to enforce the same
restrictions as primary planes had thus. The default primary plane only
expose XRBG8888 and ARGB8888 as valid pixel formats for the attached
framebuffer.

Drivers are highly recommended to implement proper support for primary
planes, and newly merged drivers must not rely upon these transitional
helpers.

The second part also implements transitional helpers which allow drivers
to gradually switch to the atomic helper infrastructure for plane
updates. Once that switch is complete drivers shouldn't use these any
longer, instead using the proper legacy implementations for update and
disable plane hooks provided by the atomic helpers.

Again drivers are strongly urged to switch to the new interfaces.

The plane helpers share the function table structures with other
helpers, specifically also the atomic helpers. See struct
``drm_plane_helper_funcs`` for the details.


Tile group
----------

Tile groups are used to represent tiled monitors with a unique integer
identifier. Tiled monitors using DisplayID v1.3 have a unique 8-byte
handle, we store this in a tile group, so we have a common identifier
for all tiles in a monitor group.


Bridges
-------


Overview
++++++++

struct ``drm_bridge`` represents a device that hangs on to an encoder.
These are handy when a regular ``drm_encoder`` entity isn't enough to
represent the entire encoder chain.

A bridge is always attached to a single ``drm_encoder`` at a time, but
can be either connected to it directly, or through an intermediate
bridge:

encoder ---> bridge B ---> bridge A

Here, the output of the encoder feeds to bridge B, and that furthers
feeds to bridge A.

The driver using the bridge is responsible to make the associations
between the encoder and bridges. Once these links are made, the bridges
will participate along with encoder functions to perform
mode_set/enable/disable through the ops provided in
``drm_bridge_funcs``.

drm_bridge, like drm_panel, aren't drm_mode_object entities like
planes, CRTCs, encoders or connectors and hence are not visible to
userspace. They just provide additional hooks to get the desired output
at the end of the encoder chain.

Bridges can also be chained up using the next pointer in struct
``drm_bridge``.

Both legacy CRTC helpers and the new atomic modeset helpers support
bridges.


Default bridge callback sequence
++++++++++++++++++++++++++++++++

The ``drm_bridge_funcs`` ops are populated by the bridge driver. The DRM
internals (atomic and CRTC helpers) use the helpers defined in
drm_bridge.c These helpers call a specific ``drm_bridge_funcs`` op for
all the bridges during encoder configuration.

For detailed specification of the bridge callbacks see
``drm_bridge_funcs``.


.. toctree::
    :maxdepth: 1

    API-drm-bridge-add
    API-drm-bridge-remove
    API-drm-bridge-attach
    API-drm-bridge-mode-fixup
    API-drm-bridge-disable
    API-drm-bridge-post-disable
    API-drm-bridge-mode-set
    API-drm-bridge-pre-enable
    API-drm-bridge-enable
    API-of-drm-find-bridge


.. _drm-kms-properties:

KMS Properties
==============

Drivers may need to expose additional parameters to applications than
those described in the previous sections. KMS supports attaching
properties to CRTCs, connectors and planes and offers a userspace API to
list, get and set the property values.

Properties are identified by a name that uniquely defines the property
purpose, and store an associated value. For all property types except
blob properties the value is a 64-bit unsigned integer.

KMS differentiates between properties and property instances. Drivers
first create properties and then create and associate individual
instances of those properties to objects. A property can be instantiated
multiple times and associated with different objects. Values are stored
in property instances, and all other property information are stored in
the property and shared between all instances of the property.

Every property is created with a type that influences how the KMS core
handles the property. Supported property types are

DRM_MODE_PROP_RANGE
    Range properties report their minimum and maximum admissible values.
    The KMS core verifies that values set by application fit in that
    range.

DRM_MODE_PROP_ENUM
    Enumerated properties take a numerical value that ranges from 0 to
    the number of enumerated values defined by the property minus one,
    and associate a free-formed string name to each value. Applications
    can retrieve the list of defined value-name pairs and use the
    numerical value to get and set property instance values.

DRM_MODE_PROP_BITMASK
    Bitmask properties are enumeration properties that additionally
    restrict all enumerated values to the 0..63 range. Bitmask property
    instance values combine one or more of the enumerated bits defined
    by the property.

DRM_MODE_PROP_BLOB
    Blob properties store a binary blob without any format restriction.
    The binary blobs are created as KMS standalone objects, and blob
    property instance values store the ID of their associated blob
    object.

    Blob properties are only used for the connector EDID property and
    cannot be created by drivers.

To create a property drivers call one of the following functions
depending on the property type. All property creation functions take
property flags and name, as well as type-specific arguments.

-  
   .. code-block:: c

       struct drm_property *drm_property_create_range(struct drm_device *dev, int flags,
                                                      const char *name,
                                                      uint64_t min, uint64_t max);

   Create a range property with the given minimum and maximum values.

-  
   .. code-block:: c

       struct drm_property *drm_property_create_enum(struct drm_device *dev, int flags,
                                                     const char *name,
                                                     const struct drm_prop_enum_list *props,
                                                     int num_values);

   Create an enumerated property. The ``props`` argument points to an
   array of ``num_values`` value-name pairs.

-  
   .. code-block:: c

       struct drm_property *drm_property_create_bitmask(struct drm_device *dev,
                                                        int flags, const char *name,
                                                        const struct drm_prop_enum_list *props,
                                                        int num_values);

   Create a bitmask property. The ``props`` argument points to an array
   of ``num_values`` value-name pairs.

Properties can additionally be created as immutable, in which case they
will be read-only for applications but can be modified by the driver. To
create an immutable property drivers must set the
DRM_MODE_PROP_IMMUTABLE flag at property creation time.

When no array of value-name pairs is readily available at property
creation time for enumerated or range properties, drivers can create the
property using the ``drm_property_create`` function and manually add
enumeration value-name pairs by calling the ``drm_property_add_enum``
function. Care must be taken to properly specify the property type
through the ``flags`` argument.

After creating properties drivers can attach property instances to CRTC,
connector and plane objects by calling the
``drm_object_attach_property``. The function takes a pointer to the
target object, a pointer to the previously created property and an
initial instance value.


Existing KMS Properties
-----------------------

The following table gives description of drm properties exposed by
various modules/drivers.



.. flat-table::
    :header-rows:  0
    :stub-columns: 0


    -  .. row 1

       -  Owner Module/Drivers

       -  Group

       -  Property Name

       -  Type

       -  Property Values

       -  Object attached

       -  Description/Restrictions

    -  .. row 2

       -  :rspan:`41` DRM

       -  Generic

       -  “rotation”

       -  BITMASK

       -  { 0, "rotate-0" }, { 1, "rotate-90" }, { 2, "rotate-180" }, { 3,
          "rotate-270" }, { 4, "reflect-x" }, { 5, "reflect-y" }

       -  CRTC, Plane

       -  rotate-(degrees) rotates the image by the specified amount in
          degrees in counter clockwise direction. reflect-x and reflect-y
          reflects the image along the specified axis prior to rotation

    -  .. row 3

       -  :rspan:`4` Connector

       -  “EDID”

       -  BLOB | IMMUTABLE

       -  0

       -  Connector

       -  Contains id of edid blob ptr object.

    -  .. row 4

       -  “DPMS”

       -  ENUM

       -  { “On”, “Standby”, “Suspend”, “Off” }

       -  Connector

       -  Contains DPMS operation mode value.

    -  .. row 5

       -  “PATH”

       -  BLOB | IMMUTABLE

       -  0

       -  Connector

       -  Contains topology path to a connector.

    -  .. row 6

       -  “TILE”

       -  BLOB | IMMUTABLE

       -  0

       -  Connector

       -  Contains tiling information for a connector.

    -  .. row 7

       -  “CRTC_ID”

       -  OBJECT

       -  DRM_MODE_OBJECT_CRTC

       -  Connector

       -  CRTC that connector is attached to (atomic)

    -  .. row 8

       -  :rspan:`10` Plane

       -  “type”

       -  ENUM | IMMUTABLE

       -  { "Overlay", "Primary", "Cursor" }

       -  Plane

       -  Plane type

    -  .. row 9

       -  “SRC_X”

       -  RANGE

       -  Min=0, Max=UINT_MAX

       -  Plane

       -  Scanout source x coordinate in 16.16 fixed point (atomic)

    -  .. row 10

       -  “SRC_Y”

       -  RANGE

       -  Min=0, Max=UINT_MAX

       -  Plane

       -  Scanout source y coordinate in 16.16 fixed point (atomic)

    -  .. row 11

       -  “SRC_W”

       -  RANGE

       -  Min=0, Max=UINT_MAX

       -  Plane

       -  Scanout source width in 16.16 fixed point (atomic)

    -  .. row 12

       -  “SRC_H”

       -  RANGE

       -  Min=0, Max=UINT_MAX

       -  Plane

       -  Scanout source height in 16.16 fixed point (atomic)

    -  .. row 13

       -  “CRTC_X”

       -  SIGNED_RANGE

       -  Min=INT_MIN, Max=INT_MAX

       -  Plane

       -  Scanout CRTC (destination) x coordinate (atomic)

    -  .. row 14

       -  “CRTC_Y”

       -  SIGNED_RANGE

       -  Min=INT_MIN, Max=INT_MAX

       -  Plane

       -  Scanout CRTC (destination) y coordinate (atomic)

    -  .. row 15

       -  “CRTC_W”

       -  RANGE

       -  Min=0, Max=UINT_MAX

       -  Plane

       -  Scanout CRTC (destination) width (atomic)

    -  .. row 16

       -  “CRTC_H”

       -  RANGE

       -  Min=0, Max=UINT_MAX

       -  Plane

       -  Scanout CRTC (destination) height (atomic)

    -  .. row 17

       -  “FB_ID”

       -  OBJECT

       -  DRM_MODE_OBJECT_FB

       -  Plane

       -  Scanout framebuffer (atomic)

    -  .. row 18

       -  “CRTC_ID”

       -  OBJECT

       -  DRM_MODE_OBJECT_CRTC

       -  Plane

       -  CRTC that plane is attached to (atomic)

    -  .. row 19

       -  :rspan:`1` DVI-I

       -  “subconnector”

       -  ENUM

       -  { “Unknown”, “DVI-D”, “DVI-A” }

       -  Connector

       -  TBD

    -  .. row 20

       -  “select subconnector”

       -  ENUM

       -  { “Automatic”, “DVI-D”, “DVI-A” }

       -  Connector

       -  TBD

    -  .. row 21

       -  :rspan:`12` TV

       -  “subconnector”

       -  ENUM

       -  { "Unknown", "Composite", "SVIDEO", "Component", "SCART" }

       -  Connector

       -  TBD

    -  .. row 22

       -  “select subconnector”

       -  ENUM

       -  { "Automatic", "Composite", "SVIDEO", "Component", "SCART" }

       -  Connector

       -  TBD

    -  .. row 23

       -  “mode”

       -  ENUM

       -  { "NTSC_M", "NTSC_J", "NTSC_443", "PAL_B" } etc.

       -  Connector

       -  TBD

    -  .. row 24

       -  “left margin”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 25

       -  “right margin”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 26

       -  “top margin”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 27

       -  “bottom margin”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 28

       -  “brightness”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 29

       -  “contrast”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 30

       -  “flicker reduction”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 31

       -  “overscan”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 32

       -  “saturation”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 33

       -  “hue”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 34

       -  :rspan:`1` Virtual GPU

       -  “suggested X”

       -  RANGE

       -  Min=0, Max=0xffffffff

       -  Connector

       -  property to suggest an X offset for a connector

    -  .. row 35

       -  “suggested Y”

       -  RANGE

       -  Min=0, Max=0xffffffff

       -  Connector

       -  property to suggest an Y offset for a connector

    -  .. row 36

       -  :rspan:`7` Optional

       -  “scaling mode”

       -  ENUM

       -  { "None", "Full", "Center", "Full aspect" }

       -  Connector

       -  TBD

    -  .. row 37

       -  "aspect ratio"

       -  ENUM

       -  { "None", "4:3", "16:9" }

       -  Connector

       -  DRM property to set aspect ratio from user space app. This enum is
          made generic to allow addition of custom aspect ratios.

    -  .. row 38

       -  “dirty”

       -  ENUM | IMMUTABLE

       -  { "Off", "On", "Annotate" }

       -  Connector

       -  TBD

    -  .. row 39

       -  “DEGAMMA_LUT”

       -  BLOB

       -  0

       -  CRTC

       -  DRM property to set the degamma lookup table (LUT) mapping pixel
          data from the framebuffer before it is given to the transformation
          matrix. The data is an interpreted as an array of struct
          drm_color_lut elements. Hardware might choose not to use the
          full precision of the LUT elements nor use all the elements of the
          LUT (for example the hardware might choose to interpolate between
          LUT[0] and LUT[4]).

    -  .. row 40

       -  “DEGAMMA_LUT_SIZE”

       -  RANGE | IMMUTABLE

       -  Min=0, Max=UINT_MAX

       -  CRTC

       -  DRM property to gives the size of the lookup table to be set on
          the DEGAMMA_LUT property (the size depends on the underlying
          hardware).

    -  .. row 41

       -  “CTM”

       -  BLOB

       -  0

       -  CRTC

       -  DRM property to set the current transformation matrix (CTM) apply
          to pixel data after the lookup through the degamma LUT and before
          the lookup through the gamma LUT. The data is an interpreted as a
          struct drm_color_ctm.

    -  .. row 42

       -  “GAMMA_LUT”

       -  BLOB

       -  0

       -  CRTC

       -  DRM property to set the gamma lookup table (LUT) mapping pixel
          data after to the transformation matrix to data sent to the
          connector. The data is an interpreted as an array of struct
          drm_color_lut elements. Hardware might choose not to use the
          full precision of the LUT elements nor use all the elements of the
          LUT (for example the hardware might choose to interpolate between
          LUT[0] and LUT[4]).

    -  .. row 43

       -  “GAMMA_LUT_SIZE”

       -  RANGE | IMMUTABLE

       -  Min=0, Max=UINT_MAX

       -  CRTC

       -  DRM property to gives the size of the lookup table to be set on
          the GAMMA_LUT property (the size depends on the underlying
          hardware).

    -  .. row 44

       -  :rspan:`19` i915

       -  :rspan:`1` Generic

       -  "Broadcast RGB"

       -  ENUM

       -  { "Automatic", "Full", "Limited 16:235" }

       -  Connector

       -  TBD

    -  .. row 45

       -  “audio”

       -  ENUM

       -  { "force-dvi", "off", "auto", "on" }

       -  Connector

       -  TBD

    -  .. row 46

       -  :rspan:`16` SDVO-TV

       -  “mode”

       -  ENUM

       -  { "NTSC_M", "NTSC_J", "NTSC_443", "PAL_B" } etc.

       -  Connector

       -  TBD

    -  .. row 47

       -  "left_margin"

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 48

       -  "right_margin"

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 49

       -  "top_margin"

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 50

       -  "bottom_margin"

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 51

       -  “hpos”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 52

       -  “vpos”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 53

       -  “contrast”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 54

       -  “saturation”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 55

       -  “hue”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 56

       -  “sharpness”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 57

       -  “flicker_filter”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 58

       -  “flicker_filter_adaptive”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 59

       -  “flicker_filter_2d”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 60

       -  “tv_chroma_filter”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 61

       -  “tv_luma_filter”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 62

       -  “dot_crawl”

       -  RANGE

       -  Min=0, Max=1

       -  Connector

       -  TBD

    -  .. row 63

       -  SDVO-TV/LVDS

       -  “brightness”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 64

       -  :rspan:`1` CDV gma-500

       -  :rspan:`1` Generic

       -  "Broadcast RGB"

       -  ENUM

       -  { “Full”, “Limited 16:235” }

       -  Connector

       -  TBD

    -  .. row 65

       -  "Broadcast RGB"

       -  ENUM

       -  { “off”, “auto”, “on” }

       -  Connector

       -  TBD

    -  .. row 66

       -  :rspan:`18` Poulsbo

       -  Generic

       -  “backlight”

       -  RANGE

       -  Min=0, Max=100

       -  Connector

       -  TBD

    -  .. row 67

       -  :rspan:`16` SDVO-TV

       -  “mode”

       -  ENUM

       -  { "NTSC_M", "NTSC_J", "NTSC_443", "PAL_B" } etc.

       -  Connector

       -  TBD

    -  .. row 68

       -  "left_margin"

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 69

       -  "right_margin"

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 70

       -  "top_margin"

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 71

       -  "bottom_margin"

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 72

       -  “hpos”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 73

       -  “vpos”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 74

       -  “contrast”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 75

       -  “saturation”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 76

       -  “hue”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 77

       -  “sharpness”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 78

       -  “flicker_filter”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 79

       -  “flicker_filter_adaptive”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 80

       -  “flicker_filter_2d”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 81

       -  “tv_chroma_filter”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 82

       -  “tv_luma_filter”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 83

       -  “dot_crawl”

       -  RANGE

       -  Min=0, Max=1

       -  Connector

       -  TBD

    -  .. row 84

       -  SDVO-TV/LVDS

       -  “brightness”

       -  RANGE

       -  Min=0, Max= SDVO dependent

       -  Connector

       -  TBD

    -  .. row 85

       -  :rspan:`10` armada

       -  :rspan:`1` CRTC

       -  "CSC_YUV"

       -  ENUM

       -  { "Auto" , "CCIR601", "CCIR709" }

       -  CRTC

       -  TBD

    -  .. row 86

       -  "CSC_RGB"

       -  ENUM

       -  { "Auto", "Computer system", "Studio" }

       -  CRTC

       -  TBD

    -  .. row 87

       -  :rspan:`8` Overlay

       -  "colorkey"

       -  RANGE

       -  Min=0, Max=0xffffff

       -  Plane

       -  TBD

    -  .. row 88

       -  "colorkey_min"

       -  RANGE

       -  Min=0, Max=0xffffff

       -  Plane

       -  TBD

    -  .. row 89

       -  "colorkey_max"

       -  RANGE

       -  Min=0, Max=0xffffff

       -  Plane

       -  TBD

    -  .. row 90

       -  "colorkey_val"

       -  RANGE

       -  Min=0, Max=0xffffff

       -  Plane

       -  TBD

    -  .. row 91

       -  "colorkey_alpha"

       -  RANGE

       -  Min=0, Max=0xffffff

       -  Plane

       -  TBD

    -  .. row 92

       -  "colorkey_mode"

       -  ENUM

       -  { "disabled", "Y component", "U component" , "V component", "RGB",
          “R component", "G component", "B component" }

       -  Plane

       -  TBD

    -  .. row 93

       -  "brightness"

       -  RANGE

       -  Min=0, Max=256 + 255

       -  Plane

       -  TBD

    -  .. row 94

       -  "contrast"

       -  RANGE

       -  Min=0, Max=0x7fff

       -  Plane

       -  TBD

    -  .. row 95

       -  "saturation"

       -  RANGE

       -  Min=0, Max=0x7fff

       -  Plane

       -  TBD

    -  .. row 96

       -  :rspan:`1` exynos

       -  CRTC

       -  “mode”

       -  ENUM

       -  { "normal", "blank" }

       -  CRTC

       -  TBD

    -  .. row 97

       -  Overlay

       -  “zpos”

       -  RANGE

       -  Min=0, Max=MAX_PLANE-1

       -  Plane

       -  TBD

    -  .. row 98

       -  :rspan:`1` i2c/ch7006_drv

       -  Generic

       -  “scale”

       -  RANGE

       -  Min=0, Max=2

       -  Connector

       -  TBD

    -  .. row 99

       -  TV

       -  “mode”

       -  ENUM

       -  { "PAL", "PAL-M","PAL-N"}, ”PAL-Nc" , "PAL-60", "NTSC-M", "NTSC-J"
          }

       -  Connector

       -  TBD

    -  .. row 100

       -  :rspan:`14` nouveau

       -  :rspan:`5` NV10 Overlay

       -  "colorkey"

       -  RANGE

       -  Min=0, Max=0x01ffffff

       -  Plane

       -  TBD

    -  .. row 101

       -  “contrast”

       -  RANGE

       -  Min=0, Max=8192-1

       -  Plane

       -  TBD

    -  .. row 102

       -  “brightness”

       -  RANGE

       -  Min=0, Max=1024

       -  Plane

       -  TBD

    -  .. row 103

       -  “hue”

       -  RANGE

       -  Min=0, Max=359

       -  Plane

       -  TBD

    -  .. row 104

       -  “saturation”

       -  RANGE

       -  Min=0, Max=8192-1

       -  Plane

       -  TBD

    -  .. row 105

       -  “iturbt_709”

       -  RANGE

       -  Min=0, Max=1

       -  Plane

       -  TBD

    -  .. row 106

       -  :rspan:`1` Nv04 Overlay

       -  “colorkey”

       -  RANGE

       -  Min=0, Max=0x01ffffff

       -  Plane

       -  TBD

    -  .. row 107

       -  “brightness”

       -  RANGE

       -  Min=0, Max=1024

       -  Plane

       -  TBD

    -  .. row 108

       -  :rspan:`6` Display

       -  “dithering mode”

       -  ENUM

       -  { "auto", "off", "on" }

       -  Connector

       -  TBD

    -  .. row 109

       -  “dithering depth”

       -  ENUM

       -  { "auto", "off", "on", "static 2x2", "dynamic 2x2", "temporal" }

       -  Connector

       -  TBD

    -  .. row 110

       -  “underscan”

       -  ENUM

       -  { "auto", "6 bpc", "8 bpc" }

       -  Connector

       -  TBD

    -  .. row 111

       -  “underscan hborder”

       -  RANGE

       -  Min=0, Max=128

       -  Connector

       -  TBD

    -  .. row 112

       -  “underscan vborder”

       -  RANGE

       -  Min=0, Max=128

       -  Connector

       -  TBD

    -  .. row 113

       -  “vibrant hue”

       -  RANGE

       -  Min=0, Max=180

       -  Connector

       -  TBD

    -  .. row 114

       -  “color vibrance”

       -  RANGE

       -  Min=0, Max=200

       -  Connector

       -  TBD

    -  .. row 115

       -  omap

       -  Generic

       -  “zorder”

       -  RANGE

       -  Min=0, Max=3

       -  CRTC, Plane

       -  TBD

    -  .. row 116

       -  qxl

       -  Generic

       -  “hotplug_mode_update"

       -  RANGE

       -  Min=0, Max=1

       -  Connector

       -  TBD

    -  .. row 117

       -  :rspan:`8` radeon

       -  DVI-I

       -  “coherent”

       -  RANGE

       -  Min=0, Max=1

       -  Connector

       -  TBD

    -  .. row 118

       -  DAC enable load detect

       -  “load detection”

       -  RANGE

       -  Min=0, Max=1

       -  Connector

       -  TBD

    -  .. row 119

       -  TV Standard

       -  "tv standard"

       -  ENUM

       -  { "ntsc", "pal", "pal-m", "pal-60", "ntsc-j" , "scart-pal",
          "pal-cn", "secam" }

       -  Connector

       -  TBD

    -  .. row 120

       -  legacy TMDS PLL detect

       -  "tmds_pll"

       -  ENUM

       -  { "driver", "bios" }

       -  -

       -  TBD

    -  .. row 121

       -  :rspan:`2` Underscan

       -  "underscan"

       -  ENUM

       -  { "off", "on", "auto" }

       -  Connector

       -  TBD

    -  .. row 122

       -  "underscan hborder"

       -  RANGE

       -  Min=0, Max=128

       -  Connector

       -  TBD

    -  .. row 123

       -  "underscan vborder"

       -  RANGE

       -  Min=0, Max=128

       -  Connector

       -  TBD

    -  .. row 124

       -  Audio

       -  “audio”

       -  ENUM

       -  { "off", "on", "auto" }

       -  Connector

       -  TBD

    -  .. row 125

       -  FMT Dithering

       -  “dither”

       -  ENUM

       -  { "off", "on" }

       -  Connector

       -  TBD

    -  .. row 126

       -  :rspan:`2` rcar-du

       -  :rspan:`2` Generic

       -  "alpha"

       -  RANGE

       -  Min=0, Max=255

       -  Plane

       -  TBD

    -  .. row 127

       -  "colorkey"

       -  RANGE

       -  Min=0, Max=0x01ffffff

       -  Plane

       -  TBD

    -  .. row 128

       -  "zpos"

       -  RANGE

       -  Min=1, Max=7

       -  Plane

       -  TBD



.. _drm-vertical-blank:

Vertical Blanking
=================

Vertical blanking plays a major role in graphics rendering. To achieve
tear-free display, users must synchronize page flips and/or rendering to
vertical blanking. The DRM API offers ioctls to perform page flips
synchronized to vertical blanking and wait for vertical blanking.

The DRM core handles most of the vertical blanking management logic,
which involves filtering out spurious interrupts, keeping race-free
blanking counters, coping with counter wrap-around and resets and
keeping use counts. It relies on the driver to generate vertical
blanking interrupts and optionally provide a hardware vertical blanking
counter. Drivers must implement the following operations.

-  
   .. code-block:: c

       int (*enable_vblank) (struct drm_device *dev, int crtc);
       void (*disable_vblank) (struct drm_device *dev, int crtc);

   Enable or disable vertical blanking interrupts for the given CRTC.

-  
   .. code-block:: c

       u32 (*get_vblank_counter) (struct drm_device *dev, int crtc);

   Retrieve the value of the vertical blanking counter for the given
   CRTC. If the hardware maintains a vertical blanking counter its value
   should be returned. Otherwise drivers can use the
   ``drm_vblank_count`` helper function to handle this operation.

Drivers must initialize the vertical blanking handling core with a call
to ``drm_vblank_init`` in their load operation. The function will set
the struct ``drm_device`` ``vblank_disable_allowed`` field to 0. This
will keep vertical blanking interrupts enabled permanently until the
first mode set operation, where ``vblank_disable_allowed`` is set to 1.
The reason behind this is not clear. Drivers can set the field to 1
after ``calling drm_vblank_init`` to make vertical blanking interrupts
dynamically managed from the beginning.

Vertical blanking interrupts can be enabled by the DRM core or by
drivers themselves (for instance to handle page flipping operations).
The DRM core maintains a vertical blanking use count to ensure that the
interrupts are not disabled while a user still needs them. To increment
the use count, drivers call ``drm_vblank_get``. Upon return vertical
blanking interrupts are guaranteed to be enabled.

To decrement the use count drivers call ``drm_vblank_put``. Only when
the use count drops to zero will the DRM core disable the vertical
blanking interrupts after a delay by scheduling a timer. The delay is
accessible through the vblankoffdelay module parameter or the
``drm_vblank_offdelay`` global variable and expressed in milliseconds.
Its default value is 5000 ms. Zero means never disable, and a negative
value means disable immediately. Drivers may override the behaviour by
setting the ``drm_device`` ``vblank_disable_immediate`` flag, which when
set causes vblank interrupts to be disabled immediately regardless of
the drm_vblank_offdelay value. The flag should only be set if there's
a properly working hardware vblank counter present.

When a vertical blanking interrupt occurs drivers only need to call the
``drm_handle_vblank`` function to account for the interrupt.

Resources allocated by ``drm_vblank_init`` must be freed with a call to
``drm_vblank_cleanup`` in the driver unload operation handler.


Vertical Blanking and Interrupt Handling Functions Reference
------------------------------------------------------------


.. toctree::
    :maxdepth: 1

    API-drm-vblank-cleanup
    API-drm-vblank-init
    API-drm-irq-install
    API-drm-irq-uninstall
    API-drm-calc-timestamping-constants
    API-drm-calc-vbltimestamp-from-scanoutpos
    API-drm-vblank-count
    API-drm-crtc-vblank-count
    API-drm-vblank-count-and-time
    API-drm-crtc-vblank-count-and-time
    API-drm-arm-vblank-event
    API-drm-crtc-arm-vblank-event
    API-drm-send-vblank-event
    API-drm-crtc-send-vblank-event
    API-drm-vblank-get
    API-drm-crtc-vblank-get
    API-drm-vblank-put
    API-drm-crtc-vblank-put
    API-drm-wait-one-vblank
    API-drm-crtc-wait-one-vblank
    API-drm-vblank-off
    API-drm-crtc-vblank-off
    API-drm-crtc-vblank-reset
    API-drm-vblank-on
    API-drm-crtc-vblank-on
    API-drm-vblank-pre-modeset
    API-drm-vblank-post-modeset
    API-drm-handle-vblank
    API-drm-crtc-handle-vblank
    API-drm-vblank-no-hw-counter
    API-drm-crtc-vblank-waitqueue


Open/Close, File Operations and IOCTLs
======================================


Open and Close
--------------


.. code-block:: c

    int (*firstopen) (struct drm_device *);
    void (*lastclose) (struct drm_device *);
    int (*open) (struct drm_device *, struct drm_file *);
    void (*preclose) (struct drm_device *, struct drm_file *);
    void (*postclose) (struct drm_device *, struct drm_file *);

    Open and close handlers. None of those methods are mandatory.

The firstopen method is called by the DRM core for legacy UMS (User Mode
Setting) drivers only when an application opens a device that has no
other opened file handle. UMS drivers can implement it to acquire device
resources. KMS drivers can't use the method and must acquire resources
in the load method instead.

Similarly the lastclose method is called when the last application
holding a file handle opened on the device closes it, for both UMS and
KMS drivers. Additionally, the method is also called at module unload
time or, for hot-pluggable devices, when the device is unplugged. The
firstopen and lastclose calls can thus be unbalanced.

The open method is called every time the device is opened by an
application. Drivers can allocate per-file private data in this method
and store them in the struct ``drm_file`` ``driver_priv`` field. Note
that the open method is called before firstopen.

The close operation is split into preclose and postclose methods.
Drivers must stop and cleanup all per-file operations in the preclose
method. For instance pending vertical blanking and page flip events must
be cancelled. No per-file operation is allowed on the file handle after
returning from the preclose method.

Finally the postclose method is called as the last step of the close
operation, right before calling the lastclose method if no other open
file handle exists for the device. Drivers that have allocated per-file
private data in the open method should free it here.

The lastclose method should restore CRTC and plane properties to default
value, so that a subsequent open of the device will not inherit state
from the previous user. It can also be used to execute delayed power
switching state changes, e.g. in conjunction with the vga_switcheroo
infrastructure (see :ref:`vga_switcheroo`). Beyond that KMS drivers
should not do any further cleanup. Only legacy UMS drivers might need to
clean up device state so that the vga console or an independent fbdev
driver could take over.


File Operations
---------------

Drivers must define the file operations structure that forms the DRM
userspace API entry point, even though most of those operations are
implemented in the DRM core. The mandatory functions are ``drm_open``,
``drm_read``, ``drm_ioctl`` and drm_compat_ioctl if CONFIG_COMPAT is
enabled. Drivers which implement private ioctls that require 32/64 bit
compatibility support must provided their onw .\ ``compat_ioctl``
handler that processes private ioctls and calls ``drm_compat_ioctl`` for
core ioctls.

In addition ``drm_read`` and ``drm_poll`` provide support for DRM
events. DRM events are a generic and extensible means to send
asynchronous events to userspace through the file descriptor. They are
used to send vblank event and page flip completions by the KMS API. But
drivers can also use it for their own needs, e.g. to signal completion
of rendering.

The memory mapping implementation will vary depending on how the driver
manages memory. Legacy drivers will use the deprecated
``drm_legacy_mmap`` function, modern drivers should use one of the
provided memory-manager specific implementations. For GEM-based drivers
this is ``drm_gem_mmap``.

No other file operations are supported by the DRM userspace API. Overall
the following is an example #file_operations structure:

static const example_drm_fops = { .owner = THIS_MODULE, .open =
drm_open, .release = drm_release, .unlocked_ioctl = drm_ioctl,
#ifdef CONFIG_COMPAT .compat_ioctl = drm_compat_ioctl, #endif .poll
= drm_poll, .read = drm_read, .llseek = no_llseek, .mmap =
drm_gem_mmap, };


.. toctree::
    :maxdepth: 1

    API-drm-open
    API-drm-release
    API-drm-read
    API-drm-poll
    API-drm-event-reserve-init-locked
    API-drm-event-reserve-init
    API-drm-event-cancel-free
    API-drm-send-event-locked
    API-drm-send-event


IOCTLs
------


.. code-block:: c

    struct drm_ioctl_desc *ioctls;
    int num_ioctls;

    Driver-specific ioctls descriptors table.

Driver-specific ioctls numbers start at DRM_COMMAND_BASE. The ioctls
descriptors table is indexed by the ioctl number offset from the base
value. Drivers can use the DRM_IOCTL_DEF_DRV() macro to initialize
the table entries.


.. code-block:: c

    DRM_IOCTL_DEF_DRV(ioctl, func, flags)

``ioctl`` is the ioctl name. Drivers must define the DRM_##ioctl and
DRM_IOCTL_##ioctl macros to the ioctl number offset from
DRM_COMMAND_BASE and the ioctl number respectively. The first macro is
private to the device while the second must be exposed to userspace in a
public header.

``func`` is a pointer to the ioctl handler function compatible with the
``drm_ioctl_t`` type.


.. code-block:: c

    typedef int drm_ioctl_t(struct drm_device *dev, void *data,
            struct drm_file *file_priv);

``flags`` is a bitmask combination of the following values. It restricts
how the ioctl is allowed to be called.

-  DRM_AUTH - Only authenticated callers allowed

-  DRM_MASTER - The ioctl can only be called on the master file handle

-  DRM_ROOT_ONLY - Only callers with the SYSADMIN capability allowed

-  DRM_CONTROL_ALLOW - The ioctl can only be called on a control
   device

-  DRM_UNLOCKED - The ioctl handler will be called without locking the
   DRM global mutex. This is the enforced default for kms drivers (i.e.
   using the DRIVER_MODESET flag) and hence shouldn't be used any more
   for new drivers.


.. toctree::
    :maxdepth: 1

    API-drm-noop
    API-drm-invalid-op
    API-drm-ioctl
    API-drm-ioctl-flags


Legacy Support Code
===================

The section very briefly covers some of the old legacy support code
which is only used by old DRM drivers which have done a so-called
shadow-attach to the underlying device instead of registering as a real
driver. This also includes some of the old generic buffer management and
command submission code. Do not use any of this in new and modern
drivers.


Legacy Suspend/Resume
---------------------

The DRM core provides some suspend/resume code, but drivers wanting full
suspend/resume support should provide save() and restore() functions.
These are called at suspend, hibernate, or resume time, and should
perform any state save or restore required by your device across suspend
or hibernate states.


.. code-block:: c

    int (*suspend) (struct drm_device *, pm_message_t state);
      int (*resume) (struct drm_device *);

Those are legacy suspend and resume methods which *only* work with the
legacy shadow-attach driver registration functions. New driver should
use the power management interface provided by their bus type (usually
through the struct ``device_driver`` dev_pm_ops) and set these methods
to NULL.


Legacy DMA Services
-------------------

This should cover how DMA mapping etc. is supported by the core. These
functions are deprecated and should not be used.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
