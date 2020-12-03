-- lists all bands with glam as their main style
SELECT band_name, IFNULL(split, year(CURDATE())) - formed as lifespan
FROM metal_bands
WHERE style LIKE 'Glam%'
ORDER BY lifespan DESC;
