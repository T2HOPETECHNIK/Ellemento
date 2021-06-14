import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, BelongsToAccessor} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {WaterHistory, WaterHistoryRelations, Location} from '../models';
import {LocationRepository} from './location.repository';

export class WaterHistoryRepository extends DefaultCrudRepository<
  WaterHistory,
  typeof WaterHistory.prototype.water_history_id,
  WaterHistoryRelations
> {

  public readonly location: BelongsToAccessor<Location, typeof WaterHistory.prototype.water_history_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('LocationRepository') protected locationRepositoryGetter: Getter<LocationRepository>,
  ) {
    super(WaterHistory, dataSource);
    this.location = this.createBelongsToAccessorFor('location', locationRepositoryGetter,);
    this.registerInclusionResolver('location', this.location.inclusionResolver);
  }
}
