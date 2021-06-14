import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, BelongsToAccessor} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {LightHistory, LightHistoryRelations, Location} from '../models';
import {LocationRepository} from './location.repository';

export class LightHistoryRepository extends DefaultCrudRepository<
  LightHistory,
  typeof LightHistory.prototype.light_history_id,
  LightHistoryRelations
> {

  public readonly location: BelongsToAccessor<Location, typeof LightHistory.prototype.light_history_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('LocationRepository') protected locationRepositoryGetter: Getter<LocationRepository>,
  ) {
    super(LightHistory, dataSource);
    this.location = this.createBelongsToAccessorFor('location', locationRepositoryGetter,);
    this.registerInclusionResolver('location', this.location.inclusionResolver);
  }
}
