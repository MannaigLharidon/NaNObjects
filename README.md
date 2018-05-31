# NaNObjects
Detect and Replace NaN objects in images

This code has been created in the case of an internship using satellite images.
Photogrammetric process did not work after having merged tiled images.

Possible reason : NaN objects.
In the main image used, there are located in the sea, which does not interest us, thus NaN objects are replaced by 0 values.

In further updates, interpolations will be developped.
