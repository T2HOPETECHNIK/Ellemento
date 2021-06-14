import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasManyRepositoryFactory, BelongsToAccessor} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {Location, LocationRelations, LocationStageAssignment, TrayMovement, Tray, LightHistory, VentilationHistory, WaterHistory, Shelf} from '../models';
import {LocationStageAssignmentRepository} from './location-stage-assignment.repository';
import {TrayMovementRepository} from './tray-movement.repository';
import {TrayRepository} from './tray.repository';
import {LightHistoryRepository} from './light-history.repository';
import {VentilationHistoryRepository} from './ventilation-history.repository';
import {WaterHistoryRepository} from './water-history.repository';
import {ShelfRepository} from './shelf.repository';

export class LocationRepository extends DefaultCrudRepository<
  Location,
  typeof Location.prototype.location_id,
  LocationRelations
> {

  public readonly locationStageAssignments: HasManyRepositoryFactory<LocationStageAssignment, typeof Location.prototype.location_id>;

  public readonly trayMovements: HasManyRepositoryFactory<TrayMovement, typeof Location.prototype.location_id>;

  public readonly trays: HasManyRepositoryFactory<Tray, typeof Location.prototype.location_id>;

  public readonly lightHistories: HasManyRepositoryFactory<LightHistory, typeof Location.prototype.location_id>;

  public readonly ventilationHistories: HasManyRepositoryFactory<VentilationHistory, typeof Location.prototype.location_id>;

  public readonly waterHistories: HasManyRepositoryFactory<WaterHistory, typeof Location.prototype.location_id>;

  public readonly shelf: BelongsToAccessor<Shelf, typeof Location.prototype.location_id>;

  public readonly location: BelongsToAccessor<LightHistory, typeof Location.prototype.location_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('LocationStageAssignmentRepository') protected locationStageAssignmentRepositoryGetter: Getter<LocationStageAssignmentRepository>, @repository.getter('TrayMovementRepository') protected trayMovementRepositoryGetter: Getter<TrayMovementRepository>, @repository.getter('TrayRepository') protected trayRepositoryGetter: Getter<TrayRepository>, @repository.getter('LightHistoryRepository') protected lightHistoryRepositoryGetter: Getter<LightHistoryRepository>, @repository.getter('VentilationHistoryRepository') protected ventilationHistoryRepositoryGetter: Getter<VentilationHistoryRepository>, @repository.getter('WaterHistoryRepository') protected waterHistoryRepositoryGetter: Getter<WaterHistoryRepository>, @repository.getter('ShelfRepository') protected shelfRepositoryGetter: Getter<ShelfRepository>,
  ) {
    super(Location, dataSource);
    this.location = this.createBelongsToAccessorFor('location', lightHistoryRepositoryGetter,);
    this.registerInclusionResolver('location', this.location.inclusionResolver);
    this.shelf = this.createBelongsToAccessorFor('shelf', shelfRepositoryGetter,);
    this.registerInclusionResolver('shelf', this.shelf.inclusionResolver);
    this.waterHistories = this.createHasManyRepositoryFactoryFor('waterHistories', waterHistoryRepositoryGetter,);
    this.registerInclusionResolver('waterHistories', this.waterHistories.inclusionResolver);
    this.ventilationHistories = this.createHasManyRepositoryFactoryFor('ventilationHistories', ventilationHistoryRepositoryGetter,);
    this.registerInclusionResolver('ventilationHistories', this.ventilationHistories.inclusionResolver);
    this.lightHistories = this.createHasManyRepositoryFactoryFor('lightHistories', lightHistoryRepositoryGetter,);
    this.registerInclusionResolver('lightHistories', this.lightHistories.inclusionResolver);
    this.trays = this.createHasManyRepositoryFactoryFor('trays', trayRepositoryGetter,);
    this.registerInclusionResolver('trays', this.trays.inclusionResolver);
    this.trayMovements = this.createHasManyRepositoryFactoryFor('trayMovements', trayMovementRepositoryGetter,);
    this.registerInclusionResolver('trayMovements', this.trayMovements.inclusionResolver);
    this.locationStageAssignments = this.createHasManyRepositoryFactoryFor('locationStageAssignments', locationStageAssignmentRepositoryGetter,);
    this.registerInclusionResolver('locationStageAssignments', this.locationStageAssignments.inclusionResolver);
  }
}
