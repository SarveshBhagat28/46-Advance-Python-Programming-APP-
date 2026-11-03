import gc
import tracemalloc

def create_objects():
    objects = []
    for number in range(10000):
        objects.append([number] * 10)
    return objects

tracemalloc.start()

print("Initial memory:", tracemalloc.get_traced_memory())

objects = create_objects()
print("After creating objects:", tracemalloc.get_traced_memory())

del objects

print("Before garbage collection:", tracemalloc.get_traced_memory())

gc.set_debug(gc.DEBUG_STATS)
collected = gc.collect()
gc.set_debug(0)

print("Collected objects:", collected)
print("After garbage collection:", tracemalloc.get_traced_memory())

print("GC thresholds:", gc.get_threshold())

gc.disable()
print("Garbage collection enabled:", gc.isenabled())

gc.enable()

print("Garbage collection enabled:", gc.isenabled())

tracemalloc.stop()
