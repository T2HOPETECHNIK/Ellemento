import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, BelongsToAccessor} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {VentilationHistory, VentilationHistoryRelations, Location} from '../models';
import {LocationRepository} from './location.repository';

export class VentilationHistoryRepository extends DefaultCrudRepository<
  VentilationHistory,
  typeof VentilationHistory.prototype.ventilation_history_id,
  VentilationHistoryRelations
> {

  public readonly location: BelongsToAccessor<Location, typeof VentilationHistory.prototype.ventilation_history_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('LocationRepository') protected locationRepositoryGetter: Getter<LocationRepository>,
  ) {
    super(VentilationHistory, dataSource);
    this.location = this.createBelongsToAccessorFor('location', locationRepositoryGetter,);
    this.registerInclusionResolver('location', this.location.inclusionResolver);
  }
}
