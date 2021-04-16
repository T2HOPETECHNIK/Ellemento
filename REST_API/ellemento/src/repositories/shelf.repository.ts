import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasManyRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {Shelf, ShelfRelations, Location} from '../models';
import {LocationRepository} from './location.repository';

export class ShelfRepository extends DefaultCrudRepository<
  Shelf,
  typeof Shelf.prototype.shelf_id,
  ShelfRelations
> {

  public readonly locations: HasManyRepositoryFactory<Location, typeof Shelf.prototype.shelf_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('LocationRepository') protected locationRepositoryGetter: Getter<LocationRepository>,
  ) {
    super(Shelf, dataSource);
    this.locations = this.createHasManyRepositoryFactoryFor('locations', locationRepositoryGetter,);
    this.registerInclusionResolver('locations', this.locations.inclusionResolver);
  }
}
